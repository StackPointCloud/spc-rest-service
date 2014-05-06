from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Architecture(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	
	# apache_none_mongo
	architecture_image = models.CharField(max_length=50, blank=False)
	
	# medium
	architecture_instance_size = models.CharField(max_length=50, blank=False)

	# small
	architecture_security_size = models.CharField(max_length=50, blank=True, default='small')

	class Meta:
		ordering = ('created',)