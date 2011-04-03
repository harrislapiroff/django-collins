from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

def register(request):
	# TODO: implement
	return render_to_response('collins/user/home.html', {}, context_instance=RequestContext(request))

@login_required
def dashboard(request):
	# TODO: implement
	return render_to_response('collins/user/home.html', {}, context_instance=RequestContext(request))

@login_required
def edit_post(request, post_pk):
	# TODO: implement
	return render_to_response('collins/user/home.html', {}, context_instance=RequestContext(request))

@login_required
def edit_blog(request, blog_slug):
	# TODO: implement
	return render_to_response('collins/user/home.html', {}, context_instance=RequestContext(request))