from django.db import models
from django.contrib.auth.models import User

class Theme(models.Model):
	title = models.CharField(max_length=50, blank=True, null=True)
	template = models.TextField()
	author = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	public = models.BooleanField()
	
	def __unicode__(self):
		return self.title if self.title else self.author.collinsprofile.__unicode__()
	
	class Meta:
		app_label = 'collins'