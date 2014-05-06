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
	architecture_image = serializers.CharField(required=True, max_length=50)
	architecture_instance_size = serializers.CharField(required=True, max_length=50)
	architecture_security_size = serializers.CharField(required=False, max_length=50)

#	class Meta:
#		model = Architecture
#		fields = ('architecture_image', 'architecture_instance_size', 'architecture_security_size')

	def restore_object(self, attrs, instance=None):
		if instance:
			instance.architecture_image = attrs.get('architecture_image', instance.architecture_image)
			instance.architecture_instance_size = attrs.get('architecture_instance_size', instance.architecture_instance_size)
			instance.architecture_security_size = attrs.get('architecture_security_size', instance.architecture_security_size)

			return instance

		return Architecture(**attrs)
