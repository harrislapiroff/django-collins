from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.db import models
from django.contrib.contenttypes.models import ContentType
from collins.models import Blog

class BlogForm(ModelForm):
	permitted_post_types = ModelMultipleChoiceField(queryset=ContentType.objects, widget=CheckboxSelectMultiple())
	class Meta:
		model = Blog
		
class CreateBlogForm(BlogForm):
	class Meta(BlogForm.Meta):
		exclude = ('admins', )