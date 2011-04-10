from collins import registry

def post_type(model, registry=registry):
	registry.register(model)
	return model