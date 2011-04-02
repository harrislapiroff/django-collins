from django.db import models
from blogs import Blog
from django.contrib.auth.models import User

class PostBase(models.Model):
	time_posted = models.DateTimeField(auto_now_add=True)
	draft = models.BooleanField(verbose_name="Draft?")
	title = models.CharField(max_length=255, blank=True, null=True)
	slug = models.SlugField()
	blog = models.ForeignKey(Blog)
	author = models.ForeignKey(User)
	class Meta:
		abstract = True
		app_label = 'collins'
		
class TextPost(PostBase):
	content = models.TextField()
	
class QuotePost(PostBase):
	content = models.TextField()
	quote_author = models.CharField(max_length=75)
	description = models.TextField(blank=True, null=True)

class LinkPost(PostBase):
	url = models.URLField()
	description = models.TextField(blank=True, null=True)
	
class ImagePost(PostBase):
	url = models.URLField()
	image = models.ImageField(upload_to='images')
	description = models.TextField(blank=True, null=True)

class ChatPost(PostBase):
	chat = models.TextField()
	description = models.TextField(blank=True, null=True)

class AudioPost(PostBase):
	audio = models.FileField(upload_to='audio')
	description = models.TextField(blank=True, null=True)

class VideoFilePost(PostBase):
	video = models.FileField(upload_to='video')
	description = models.TextField(blank=True, null=True)

class VideoExternalPost(PostBase):
	embed_code = models.TextField()
	description = models.TextField(blank=True, null=True)

class CodePost(PostBase):
	code = models.TextField()
	description = models.TextField(blank=True, null=True)
