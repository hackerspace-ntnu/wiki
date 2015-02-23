from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HSWiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('hsauth.urls')),
    url(r'^accounts/profile/$', 'wiki-extra.views.index'),
)

from wiki.urls import get_pattern as get_wiki_pattern
urlpatterns += patterns('',
                        (r'', get_wiki_pattern())
                        ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
