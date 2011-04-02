from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class Blog(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	admins = models.ManyToManyField(User)
	date_created = models.DateTimeField(auto_now_add=True)
	custom_domain = models.OneToOneField(Site, blank=True, null=True, related_name='Primary Blog')
	class Meta:
		app_label = 'collins'