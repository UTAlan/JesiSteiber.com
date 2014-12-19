from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from badges.models import Badge
from blog.models import Post
from links.models import Link
from verses.models import Verse

def index(request):
    info = {}
    
    if request.user.is_authenticated():
        all_posts = Post.objects.filter(is_public=True).filter(Q(groups__in=request.user.groups.all()) | Q(groups__isnull=True)).order_by('-created_date')
    else:
       all_posts = Post.objects.filter(is_public=True).filter(groups__isnull=True).order_by('-created_date')
    info['posts'] = all_posts[:1]
     
    info['links'] = Link.objects.filter(is_public=True)
    
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    info['badges'] = Badge.objects.filter(is_public=True)
    
    info['active'] = 'index'
    
    return render_to_response('index.html', { 'info': info }, context_instance=RequestContext(request))
