from django.conf.urls import patterns

urlpatterns = patterns('photos.views',
    (r'^$', 'index'),
    (r'^(?P<album_id>[0-9]+)/$', 'album'),
)
