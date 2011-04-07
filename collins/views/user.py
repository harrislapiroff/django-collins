from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseForbidden
from collins.models import Blog, User
from collins.forms import CreateBlogForm
from collins.settings import COLLINS_USER_REGISTRATION

def register(request):
	if not COLLINS_USER_REGISTRATION:
		return HttpResponseForbidden(u'User registration is not permitted on this site because <code>settings.COLLINS_USER_REGISTRATION</code> is false.')
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
	profile = request.user.get_profile()
	user_blogs = request.user.blogs.all()
	current_blog = profile.last_managed_blog if profile.last_managed_blog else user_blogs[0] if user_blogs.count() != 0 else None
	cx = {
		'blogs': user_blogs,
		'current_blog': current_blog
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
	# if the form has been submitted
	if request.method == 'POST':
		form = CreateBlogForm(request.POST)
		if form.is_valid():
			# save the form as an object
			blog = form.save()
			# add the current user as an admin
			blog.admins.add(request.user)
			# save it again!
			blog.save()
			# then redirect to the appropriate manage blog posts page
			return HttpResponseRedirect(reverse('manage_blog_posts', kwargs = {'blog_slug': blog.slug}))
		else:
			return render_to_response('collins/user/form.html', {'form': form, 'title': "Create a blog", 'button_text': "Create Blog"}, context_instance=RequestContext(request))
	# if the form has not been submitted
	else:
		form = CreateBlogForm()
		return render_to_response('collins/user/form.html', {'form': form, 'title': "Create a blog", 'button_text': "Create Blog"}, context_instance=RequestContext(request))


@login_required
def edit_blog(request, blog_slug):
	pass

@login_required
def manage_blog_posts(request, blog_slug):
	"""
	Changes the current user's profile.last_managed blog to the blog_slug
	requested and redirects back to the dashboard.
	"""
	profile = request.user.get_profile()
	blog = Blog.objects.filter(slug__exact=blog_slug)[0]
	profile.last_managed_blog = blog
	profile.save()
	return HttpResponseRedirect(reverse('dashboard'))