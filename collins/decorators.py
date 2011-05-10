from collins import registry
from django.forms import ModelForm

def post_type(model, form=None, registry=registry):
	registry.register(model, form)
	return model