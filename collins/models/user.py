from django.db import models
from django.contrib.auth.models import User, UserManager
from collins.models import Blog

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	last_managed_blog = models.ForeignKey(Blog, blank=True, null=True)
	class Meta:
		app_label = 'collins'