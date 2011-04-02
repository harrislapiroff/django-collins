from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('collins.views',
	url(r'(?<blog_slug>[\w-]*)/?', 'blog'),
	url(r'(?<blog_slug>[\w-]*)/(?<post_pk>[0-9]*)/[\w-]*/?', 'post'),
)