from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.defaults import page_not_found, server_error

from main import views as mainviews

try:
    from django.conf.urls import url, patterns, include
# Support Django<=1.5
except ImportError:
    from django.conf.urls.defaults import url, patterns, include


# 404 and 500 handlers
handler404 = page_not_found
handler500 = server_error

# Project urls
urlpatterns = patterns('',
                       url('^$', mainviews.Index.as_view(), name='index'),
                       url('^logout/$',
                           'django.contrib.auth.views.logout', name='logout'),
                       )

# Django admin
admin.autodiscover()
urlpatterns += [url(r'^admin/', include(admin.site.urls)), ]

# Debug static files serve
urlpatterns += staticfiles_urlpatterns()
