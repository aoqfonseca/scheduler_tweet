from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from tweet.views import callback_twitter, busca_token

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^twitter/(?P<configuracao_id>.*)$', callback_twitter),
                       url(r'^pega_token/(?P<configuracao_id>.*)$', busca_token),
                       )

urlpatterns += staticfiles_urlpatterns()
