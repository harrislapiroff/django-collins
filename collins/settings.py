from django.conf import settings

ALLOW_USER_REGISTRATION = getattr(settings, 'ALLOW_USER_REGISTRATION', True)