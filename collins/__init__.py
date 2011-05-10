from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
import operator


class AlreadyRegistered(Exception):
	pass


class NotRegistered(Exception):
	pass


class PostTypeRegistry(object):
	def __init__(self):
		self._registry = {}

	def register(self, model):
		if model in self._registry:
			raise AlreadyRegistered('Post type %s is already registered.' % model)

		self._registry[model] = model

	def unregister(self, model):
		if model not in self._registry:
			raise NotRegistered('Post type %s is not registered.' % model)

		self._registry.remove(PostType)

	def __iter__(self):
		return self._registry.__iter__()

	def items(self):
		return self._registry.items()

	def __getitem__(self, key):
		return self._registry[key]
	
	def content_types_lookup(self):
		"""
		Returns a Q object for looking up content types of all post types.
		Comes in handy, especially in "limit_choices_to" on models.
		"""
		qs = [Q(model__iexact=model.__name__) for (key, model) in self.items()]
		# http://www.djangozen.com/blog/the-power-of-q
		return reduce(operator.or_, qs)
		
	def content_types(self):
		"""
		Returns a list of content types corresponding to post types.
		"""
		return ContentType.objects.filter(self.content_types_lookup())

registry = PostTypeRegistry()