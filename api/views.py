import pika

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, ArchitectureSerializer
from django.http import HttpResponse
from api.models import Architecture
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging

logging.basicConfig()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ArchitectureViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows an architecture to be deployed.
	"""
	queryset = Architecture.objects.all()
	serializer_class = ArchitectureSerializer

@api_view(['GET', 'POST'])
def architecture_list(request, format=None):
    """
    List all architecture requests or create a new one.
    """
    if request.method == 'GET':
        architectures = Architecture.objects.all()
        serializer = ArchitectureSerializer(architectures, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
    	serializer = ArchitectureSerializer(data=request.DATA)
        if serializer.is_valid():
            #credentials = pika.PlainCredentials('stackpointcloud', 'stackpointcloud')
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))
            channel = connection.channel()
            channel.queue_declare(queue='hello')
            channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
            connection.close()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def architecture_detail(request, pk, format=None):
    """
    Retrieve, update, or delete an architecture request.
    """
    try:
        architecture = Architecture.objects.get(pk=pk)
    except Architecture.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArchitectureSerializer(architecture)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArchitectureSerializer(architecture, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        architecture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)