from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Architecture, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ArchitectureSerializer(serializers.Serializer):
	pk = serializers.Field()

	architecture_image = serializers.CharField(required=True, 
		                                       max_length=50)

	architecture_instance_size = serializers.CharField(required=True,
		                                               max_length=50)
