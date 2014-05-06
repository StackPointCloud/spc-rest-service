import pika
import logging

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, ArchitectureSerializer
from django.http import HttpResponse
from api.models import Architecture
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

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

class ArchitectureList(APIView):
    def get(self, request, format=None):
        architectures = Architecture.objects.all()
        serializer = ArchitectureSerializer(architectures, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
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

class ArchitectureDetail(APIView):
    def get_object(self, pk):
        try:
            return Architecture.objects.get(pk=pk)
        except Architecture.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        architecture = get_object(pk)
        serializer = ArchitectureSerializer(architecture)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
    	architecture = get_object(pk)
    	serializer = ArchitectureSerializer(architecture, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
    	architecture = get_object(pk)
    	architecture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)