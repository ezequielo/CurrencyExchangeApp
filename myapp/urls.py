from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('currencyapp.urls')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout')
)
