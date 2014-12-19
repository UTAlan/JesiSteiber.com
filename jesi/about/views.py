from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from verses.models import Verse
from links.models import Link

def index(request):
    info = {}
    
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    info['links'] = Link.objects.filter(is_public=True)
    
    info['active'] = 'about'
    
    return render_to_response('about/index.html', { 'info': info }, context_instance=RequestContext(request))
