from django.db.models.loading import AppCache
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseForbidden
from collins.models import Blog, User
from collins.forms import CreateBlogForm, PostShellForm, BasePostForm
from django.forms.models import modelform_factory
from collins.settings import COLLINS_USER_REGISTRATION, COLLINS_LOGIN_URL

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

@login_required(login_url=COLLINS_LOGIN_URL)
def dashboard(request):
	profile = request.user.collinsprofile
	user_blogs = request.user.blogs.all()
	current_blog = profile.last_managed_blog if profile.last_managed_blog else user_blogs[0] if user_blogs.count() != 0 else None
	cx = {
		'blogs': user_blogs,
		'current_blog': current_blog
	}
	return render_to_response('collins/user/dashboard.html', cx, context_instance=RequestContext(request))

@login_required(login_url=COLLINS_LOGIN_URL)
def create_post(request, blog_slug, post_type):
	post_content_type = ContentType.objects.get(model=post_type)
	post_model = post_content_type.model_class()
	PostForm = modelform_factory(post_model)

	if request.method == 'POST':
		shell_form = PostShellForm(request.POST)
		post_form = PostForm(request.POST)
		if post_form.is_valid() and shell_form.is_valid():
			post = post_form.save()
			post_shell = post_form.save(commit=False)
			post_shell.post_content_type = post_content_type
			post_shell.post_content_id = post.id
			post_shell.author = request.user
			post_shell.blog = request.user.collinsprofile.last_managed_blog
			post_shell.save()
			return HttpResponseRedirect(reverse('dashboard'))
		else:
			return render_to_response('collins/user/postform.html', {'shell_form': shell_form, 'post_form': post_form, 'button_text': 'Create Post'}, context_instance=RequestContext(request))
	else:
		shell_form = PostShellForm()
		post_form = PostForm()
		return render_to_response('collins/user/postform.html', {'shell_form': shell_form, 'post_form': post_form, 'button_text': 'Create Post'}, context_instance=RequestContext(request))


@login_required(login_url=COLLINS_LOGIN_URL)
def edit_post(request, post_pk):
	# TODO: implement
	return render_to_response('collins/user/home.html', {}, context_instance=RequestContext(request))

@login_required(login_url=COLLINS_LOGIN_URL)
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


@login_required(login_url=COLLINS_LOGIN_URL)
def edit_blog(request, blog_slug):
	pass

@login_required(login_url=COLLINS_LOGIN_URL)
def manage_blog_posts(request, blog_slug):
	"""
	Changes the current user's profile.last_managed blog to the blog_slug
	requested and redirects back to the dashboard.
	"""
	profile = request.user.collinsprofile
	blog = Blog.objects.filter(slug__exact=blog_slug)[0]
	profile.last_managed_blog = blog
	profile.save()
	return HttpResponseRedirect(reverse('dashboard'))