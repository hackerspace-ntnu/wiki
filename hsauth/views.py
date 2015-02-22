from allaccess.views import OAuthCallback
from django.views.generic import View
from django.contrib.auth import authenticate, login, get_user_model
import logging

from django.core.urlresolvers import reverse
from allaccess.views import OAuthRedirect

# Create your views here.

logger = logging.getLogger('hsauth.views')


class HSAuthRedirect(OAuthRedirect):
    def get_callback_url(self, provider):
        return reverse('associate-callback', kwargs={'provider': provider.name})


class HSCallback(OAuthCallback, View):
    def get_or_create_user(self, provider, access, info):
        "Create a shell auth.User."
        username = info.get("username")
        User = get_user_model()
        kwargs = {
            User.USERNAME_FIELD: username,
            'email': info.get('email'),
            'password': None,
            'first_name': info.get('first_name'),
            'last_name': info.get('last_name')
        }
        return User.objects.create_user(**kwargs)