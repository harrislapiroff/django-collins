from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

def register(request):
	# TODO: implement
	return render_to_response('collins/user/home.html')

@login_required(login_url='/login/')
def dashboard(request):
	# TODO: implement
	return render_to_response('collins/user/home.html')

@login_required(login_url='/login/')
def edit_post(request, post_pk):
	# TODO: implement
	return render_to_response('collins/user/home.html')

@login_required(login_url='/login/')
def edit_blog(request, blog_slug):
	# TODO: implement
	return render_to_response('collins/user/home.html')