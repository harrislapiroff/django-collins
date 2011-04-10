from django import forms
from django.db import models
from django.contrib.contenttypes.models import ContentType
from collins.models import Blog, PostShell
from collins import registry

class BlogForm(forms.ModelForm):
	permitted_post_types = forms.ModelMultipleChoiceField(queryset=registry.content_types(), widget=forms.CheckboxSelectMultiple())
	slug = forms.SlugField(label=u'Blog URL',)
	class Meta:
		model = Blog
		
class CreateBlogForm(BlogForm):
	class Meta(BlogForm.Meta):
		exclude = ('admins', )


class PostForm(forms.ModelForm):
	pass
	
class PostShellForm(forms.ModelForm):
	class Meta:
		model = PostShell