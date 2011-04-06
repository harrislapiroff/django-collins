from django.forms import ModelForm
from collins.models import Blog

class BlogForm(ModelForm):
	class Meta:
		model = Blog
		
class CreateBlogForm(ModelForm):
	class Meta:
		model = Blog
		exclude = ('admins', )