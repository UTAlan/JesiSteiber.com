from django.contrib.syndication.views import Feed
from blog.models import Post

class LatestBlogs(Feed):
    title = "JessicaSteiber.com"
    link = "http://www.jessicasteiber.com"
    description = "JessicaSteiber.com Blog"

    def items(self):
        return Post.objects.filter(is_public=True).filter(groups__isnull=True).order_by('-created_date')[:5]
    
    def item_description(self, item):
        return '<p>' + item.content.replace('\n', '</p>\n<p>') + '</p>'
