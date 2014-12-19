from django.conf.urls import patterns, url

urlpatterns = patterns('about.views',
    (r'^$', 'index'),
)
