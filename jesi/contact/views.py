from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render_to_response, redirect
from django.shortcuts import render
from django.template import RequestContext
from contact.models import ContactForm
from recaptcha.client import captcha
from verses.models import Verse
from links.models import Link


def index(request):
    info = {}
    
    info['links'] = Link.objects.filter(is_public=True)
    
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            r = captcha.submit(request.POST['recaptcha_challenge_field'], request.POST['recaptcha_response_field'], settings.RECAPTCHA_PRIVATE_KEY, request.META['REMOTE_ADDR'])
            if not r.is_valid:
                return redirect('/contact/') # Invalid form entry
            
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients = ['jesi@jessicasteiber.com', 'alan@alanbeam.net']
            
            email = EmailMessage('Contact Message From ' + name + ' - JessicaSteiber.com', message, email, recipients)
            email.send()
            
            info['msg'] = '<p class="success">Message successfully sent.</p>'
            info['form'] = ContactForm()
    else:
        info['form'] = ContactForm() # An unbound form
        info['msg'] = ''
    
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    info['active'] = 'contact'
    
    return render_to_response('contact/index.html', { 'info': info }, context_instance=RequestContext(request))
