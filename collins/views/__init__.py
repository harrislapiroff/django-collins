from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

def home(request):
	# TODO: this should be a three-way switch
	# 1: if a primary blog is set on the site, run the blog view
	# 2: otherwise, if a user is not logged display a register/sign in page
	# 3: if the user is logged in and there is no primary blog, redirect to user interface
	return render_to_response('collins/user/home.html')