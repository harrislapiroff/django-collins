from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.http import HttpResponseRedirect
from collins.models import Blog, User

def register(request):
	if request.user.is_authenticated(): # if the user is already logged in
		return HttpResponseRedirect(reverse('dashboard'))
	elif not request.method == 'POST': # if the form has not been submitted yet
		return render_to_response('collins/user/register.html', {'form': UserCreationForm()}, context_instance=RequestContext(request))
	else:
		form = UserCreationForm(request.POST)
		if not form.is_valid():
			return render_to_response('collins/user/register.html', {'form': form}, context_instance=RequestContext(request))
		else:
			user = form.save()
			user = authenticate(username = user.username, password = form.data['password1'])
			login(request, user)
			return HttpResponseRedirect(reverse('create_blog'))

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