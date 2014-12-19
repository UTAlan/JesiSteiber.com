from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from verses.models import Verse

def index(request):
    return redirect('/profile/');

def register(request):
    if request.user.is_authenticated():
        return redirect('/accounts/profile/')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            if user is not None:
                # Add user to REGISTERED_USERS group
                default_group = Group.objects.get(pk=1)
                user.groups.add(default_group)
                user.save()
                # Log User In
                login(request, user)
                # Redirect to home page
                return redirect('/')
    else:
        form = UserCreationForm()
    
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    return render_to_response('registration/register.html', { 'form':form }, context_instance=RequestContext(request))

def profile(request):
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    return render_to_response('registration/profile.html', { }, context_instance=RequestContext(request))
