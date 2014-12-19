from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'index'),
    url(r'^page/(?P<page_id>[\d]+)/$', 'index'),
    url(r'^cat/(?P<cat_name>[^/]+)/$', 'category'),
    url(r'^tag/(?P<cat_name>[^/]+)/page/(?P<page_id>[\d]+)/$', 'category'),
    url(r'^tag/(?P<tag_name>[^/]+)/$', 'tag'),
    url(r'^tag/(?P<tag_name>[^/]+)/page/(?P<page_id>[\d]+)/$', 'tag'),
    url(r'^(?P<post_id>[\d]+)/$', 'detail'),
    url(r'^(?P<post_id>[\d]+)/comment/$', 'comment'),
)
