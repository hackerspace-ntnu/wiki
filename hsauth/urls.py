from hsauth.views import HSAuthRedirect, HSCallback

__author__ = 'CVi'

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^login/(?P<provider>(\w|-)+)/$', login_required(HSAuthRedirect.as_view()), name='associate'),
                       url(r'^callback/(?P<provider>(\w|-)+)/$', login_required(HSCallback.as_view()), name='associate-callback'),
                       )
