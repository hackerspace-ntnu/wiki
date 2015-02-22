from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from hsauth.views import HSCallback

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HSWiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('hsauth.urls')),

)
