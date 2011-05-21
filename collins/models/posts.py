from django.db import models
from django.forms.models import modelform_factory
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from collins import registry as post_types
from collins.models.blogs import Blog


class PostShell(models.Model):
	time_posted = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique=True)
	blog = models.ForeignKey(Blog, related_name='posts')
	draft = models.BooleanField(verbose_name="Draft?")
	author = models.ForeignKey(User)
	post_content_type = models.ForeignKey(ContentType)
	post_content_id = models.IntegerField()
	post_content_object = generic.GenericForeignKey('post_content_type', 'post_content_id')
	
	def typename(self):
		return type(self).__name__

	def data(self):
		return self.post_content_object

	def __unicode__(self):
		return u"%s (%s)" % (
			self.post_content_object.__unicode__(),
			self.post_content_type.name
		)

	class Meta:
		app_label = 'collins'


class PostBase(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	shell = generic.GenericRelation(PostShell, content_type_field = 'post_content_type', object_id_field = 'post_content_id')
	
	def published(self):
		return self.shell.all()[0].time_posted
		
	@classmethod
	def get_form(cls):
		return modelform_factory(cls)

	def __unicode__(self):
		title_bits = []
		shell = self.shell.all()[0]
		
		title_bits.extend([
			shell.blog.name,
			': '
		])
		if self.title:
			title_bits.append(self.title)
		else:
			title_bits.append('Post %d' % self.pk)
		
		return "".join(title_bits)
	
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

post_types.register(TextPost)
post_types.register(QuotePost)
post_types.register(LinkPost)
post_types.register(ImagePost)
post_types.register(ChatPost)
post_types.register(AudioPost)
post_types.register(VideoFilePost)
post_types.register(VideoExternalPost)
post_types.register(CodePost)