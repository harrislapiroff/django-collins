from collins import registry
from django.forms import ModelForm

def post_type(model, registry=registry):
	registry.register(model)
	return model