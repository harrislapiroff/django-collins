from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class Blog(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)
	description = models.TextField(blank=True, null=True)
	admins = models.ManyToManyField(User, related_name='blogs')
	date_created = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		app_label = 'collins'
		
models.ForeignKey(Blog, blank=True, null=True, related_name='Custom Domain').contribute_to_class(Site, 'primary_blog')