from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from collins.models import Blog, User

def register(request):
	# TODO: implement
	return render_to_response('collins/user/home.html', {}, context_instance=RequestContext(request))

@login_required
def dashboard(request):
	user_blogs = request.user.blogs.all()
	cx = {
		'blogs': user_blogs
	}
	return render_to_response('collins/user/dashboard.html', cx, context_instance=RequestContext(request))

@login_required
def create_post(request, post_pk):
	# TODO: implement
	return render_to_response('collins/user/home.html', {}, context_instance=RequestContext(request))


@login_required
def edit_post(request, post_pk):
	# TODO: implement
	return render_to_response('collins/user/home.html', {}, context_instance=RequestContext(request))

@login_required
def create_blog(request):
	# TODO: implement
	pass

@login_required
def edit_blog(request, blog_slug):
	# TODO: implement
	return render_to_response('collins/user/home.html', {}, context_instance=RequestContext(request))

@login_required
def manage_blog_posts(request, blog_slug):
	# TODO: implement
	# 1 check if they own the blog
	# 2 get the posts and render them with controls
	pass