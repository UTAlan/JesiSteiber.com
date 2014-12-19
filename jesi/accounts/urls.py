from django.conf.urls import patterns
from django.conf import settings
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('accounts.views',
    (r'^$', 'index'),
    (r'^profile/', 'profile'),
    (r'^register/$', 'register'),
)
