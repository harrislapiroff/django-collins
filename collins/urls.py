from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('collins.views',
	url(r'$', 'home'),
	url(r'(?P<post_pk>[0-9]*)/[\w-]*/$', 'blog.post'),
	url(r'(?P<blog_slug>[\w-]*)/$', 'blog.blog'),
	url(r'(?P<blog_slug>[\w-]*)/(?P<post_pk>[0-9]*)/[\w-]*/$', 'blog.post'),
)