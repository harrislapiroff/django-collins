from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	admins = models.ManyToManyField(User)
	date_created = models.DateTimeField(auto_now_add=True)
	class Meta:
		app_label = 'collins'