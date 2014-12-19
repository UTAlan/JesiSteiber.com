from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from gdata.photos import service
from links.models import Link
from verses.models import Verse

def index(request):
    info = {}
        
    gd_client = service.PhotosService()
    gd_client.email = settings.GOOGLE_EMAIL
    gd_client.password = settings.GOOGLE_PASS
    gd_client.source = settings.SITE_NAME
    gd_client.ProgrammaticLogin()
    
    albums = gd_client.GetUserFeed()
    info['albums'] = []
    for album in albums.entry:
      if album.rights.text == 'public':
        a = {}
        a['title'] = album.title.text
        a['thumb'] = album.media.thumbnail[0].url
        a['id'] = album.gphoto_id.text
        info['albums'].append(a)
    
    info['albums'].sort()
    
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    info['links'] = Link.objects.filter(is_public=True)
    
    info['active'] = 'photos'
    
    return render_to_response('photos/index.html', { 'info': info }, context_instance=RequestContext(request))

def album(request, album_id):
    info = {}
    
    gd_client = service.PhotosService()
    gd_client.email = settings.GOOGLE_EMAIL
    gd_client.password = settings.GOOGLE_PASS
    gd_client.source = settings.SITE_NAME
    gd_client.ProgrammaticLogin()
    
    album = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s' % (settings.GOOGLE_USER, album_id))
    info['album'] = {}
    info['album']['title'] = album.title.text
    info['album']['id'] = album_id
    
    photos = gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?kind=photo' % (settings.GOOGLE_USER, album_id))
    
    info['photos'] = []
    for photo in photos.entry:
      p = {}
      p['caption'] = photo.media.description.text
      p['thumb'] = photo.media.thumbnail[1].url
      p['img'] = photo.content.src
      p['id'] = photo.gphoto_id.text
      info['photos'].append(p)
    
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    info['links'] = Link.objects.filter(is_public=True)
    
    info['active'] = 'photos'
    
    return render_to_response('photos/album.html', { 'info': info }, context_instance=RequestContext(request))
