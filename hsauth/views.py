from allaccess.views import OAuthCallback
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, get_user_model
import logging

from django.core.urlresolvers import reverse
from allaccess.views import OAuthRedirect

# Create your views here.

logger = logging.getLogger('hsauth.views')


class HSAuthRedirect(OAuthRedirect):
    def get_callback_url(self, provider):
        print(reverse('associate-callback', kwargs={'provider': provider.name}))
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

    def handle_existing_user(self, provider, user, access, info):
        "Login user and redirect."
        login(self.request, user)
        s = False
        print("Hello")
        if user.email != info.get('email'):
            user.email = info.get('email')
            s = True
        if user.first_name != info.get('first_name'):
            user.first_name = info.get('first_name')
            s = True
        if user.last_name != info.get('last_name'):
            user.last_name = info.get('last_name')
            s = True
        if s:
            user.save()
        return redirect(self.get_login_redirect(provider, user, access))