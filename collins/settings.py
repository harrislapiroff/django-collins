from django.conf import settings
from django.core.urlresolvers import reverse

COLLINS_USER_REGISTRATION = getattr(settings, 'COLLINS_USER_REGISTRATION', True)
# allow for a custom settings.COLLINS_LOGIN_URL but default to settings.LOGIN_URL
COLLINS_LOGIN_URL = getattr(settings, 'COLLINS_LOGIN_URL', getattr(settings, 'LOGIN_URL', '/accounts/login/'))