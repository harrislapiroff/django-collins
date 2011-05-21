from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from collins import registry
from collins.models.themes import Theme

class Blog(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)
	description = models.TextField(blank=True, null=True)
	admins = models.ManyToManyField(User, related_name='blogs')
	date_created = models.DateTimeField(auto_now_add=True)
	# TODO: limit this to only ContentTypes which are registered as PostBase
	permitted_post_types = models.ManyToManyField(ContentType)
	theme = models.ForeignKey(Theme, default=1)
	
	def get_posts(self):
		return self.posts.objects.all()
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		app_label = 'collins'
		
models.ForeignKey(Blog, blank=True, null=True, related_name='Custom Domain').contribute_to_class(Site, 'primary_blog')