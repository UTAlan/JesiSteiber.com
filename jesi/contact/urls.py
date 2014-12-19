from django.conf.urls import patterns

urlpatterns = patterns('contact.views',
    (r'^$', 'index'),
)
