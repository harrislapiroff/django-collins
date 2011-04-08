from django.conf.urls.defaults import patterns, include, url
from django.core.urlresolvers import reverse

urlpatterns = patterns('collins.views',
	url(r'^$', 'home', name = u'home'),
)

urlpatterns += patterns('django.contrib.auth.views',
	url(r'^login/$', 'login', {
		'template_name': 'collins/user/login.html',
	}, name=u'login'),
	url(r'^logout/$', 'logout_then_login', name = u'logout'),
)

urlpatterns += patterns('collins.views.user',
	url(r'^register/$', 'register', name = u'register'),
	url(r'^dashboard/$', 'dashboard', name = u'dashboard'),
	url(r'^create/$', 'create_blog', name = u'create_blog'),
	url(r'^post/(?P<post_pk>[0-9]*)/edit/$', 'edit_post', name = u'edit_post'),
	url(r'^blog/(?P<blog_slug>[\w-]*)/settings/$', 'edit_blog', name = u'edit_blog'),
	url(r'^blog/(?P<blog_slug>[\w-]*)/posts/$', 'manage_blog_posts', name = u'manage_blog_posts'),
	url(r'^blog/(?P<blog_slug>[\w-]*)/new/(?P<post_type>[\w_-]*)/$', 'create_post', name = u'create_post'),
) 

urlpatterns += patterns('collins.views.blog',
	url(r'^(?P<post_pk>[0-9]*)/[\w-]*/$', 'post'),
	url(r'^(?P<blog_slug>[\w-]*)/$', 'blog'),
	url(r'^(?P<blog_slug>[\w-]*)/(?P<post_pk>[0-9]*)/[\w-]*/$', 'post'),
)