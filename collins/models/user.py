from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, UserManager
from collins.models import Blog

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True, related_name='Collins Profile')
	last_managed_blog = models.ForeignKey(Blog, blank=True, null=True)
	
	def __unicode__(self):
		name = self.user.get_full_name()
		return name if name else self.user.username
	
	class Meta:
		app_label = 'collins'
		
@receiver(post_save, sender=User)
def update_user_profile(sender, **kwargs):
	user = kwargs['instance']
	try:
		user.get_profile()
	except:
		profile = UserProfile(user=user)
		profile.save()