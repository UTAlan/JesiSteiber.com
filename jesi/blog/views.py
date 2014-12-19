from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.conf import settings
from blog.models import Category, Tag, Post, Comment
from blog.forms import CommentForm
from recaptcha.client import captcha
from django.core.mail import send_mail
from django.contrib.auth.models import User
from links.models import Link
from verses.models import Verse
import math

def index(request, page_id=1):
    info = {}
    per_page = 5
    
    if request.user.is_authenticated():
        all_posts = Post.objects.filter(is_public=True).filter(Q(groups__in=request.user.groups.all()) | Q(groups__isnull=True)).order_by('-created_date')
    else:
        all_posts = Post.objects.filter(is_public=True).filter(groups__isnull=True).order_by('-created_date')
    
    paginator = Paginator(all_posts, per_page)
    
    try:
      page = int(page_id)
    except ValueError:
      page = 1
    
    try:
      info['posts'] = paginator.page(page)
    except (EmptyPage, InvalidPage):
      info['posts'] = paginator.page(paginator.num_pages)
    
    for post in info['posts'].object_list:
        post.comment_list = Comment.objects.filter(post=post)
    
    info['links'] = Link.objects.filter(is_public=True)
    
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    info['active'] = 'blog'
    
    return render_to_response('blog/index.html', { 'info': info }, context_instance=RequestContext(request))

def category(request, cat_name, page_id=1):
    info = {}
    
    info['page_id'] = int(page_id)
    start_index = 5 * (info['page_id'] - 1)
    end_index = start_index + 5
    
    cat = Category.objects.get(title=cat_name)
    
    if request.user.is_authenticated():
        all_posts = Post.objects.filter(is_public=True).filter(Q(groups__in=request.user.groups.all()) | Q(groups__isnull=True)).filter(category=cat).order_by('created_date')
    else:
        all_posts = Post.objects.filter(is_public=True).filter(groups__isnull=True).filter(category=cat).order_by('-created_date')
    
    info['posts'] = all_posts[start_index:end_index]
    info['num_pages'] = math.ceil(all_posts.count() / 5.0)
    
    info['blog_nav'] = True
    if info['page_id'] == 1:
        if info['page_id'] == info['num_pages']:
            info['blog_nav'] = False
    
    # If invalid page number, redirect to home page
    if info['posts'].count() == 0:
        return redirect('/')
    
    for post in info['posts']:
        post.comment_list = Comment.objects.filter(post=post)
    
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    info['active'] = 'blog'
    
    return render_to_response('blog/index.html', { 'info': info }, context_instance=RequestContext(request))

def tag(request, tag_name, page_id=1):
    info = {}
    
    info['page_id'] = int(page_id)
    start_index = 5 * (info['page_id'] - 1)
    end_index = start_index + 5
    
    tag = Tag.objects.get(title=tag_name)
    
    if request.user.is_authenticated():
        all_posts = Post.objects.filter(is_public=True).filter(Q(groups__in=request.user.groups.all()) | Q(groups__isnull=True)).filter(tags=tag.id).order_by('created_date')
    else:
        all_posts = Post.objects.filter(is_public=True).filter(groups__isnull=True).filter(tags=tag.id).order_by('-created_date')
    
    info['posts'] = all_posts[start_index:end_index]
    info['num_pages'] = math.ceil(all_posts.count() / 5.0)
    
    info['blog_nav'] = True
    if info['page_id'] == 1:
        if info['page_id'] == info['num_pages']:
            info['blog_nav'] = False
    
    # If invalid page number, redirect to home page
    if info['posts'].count() == 0:
        return redirect('/')
    
    for post in info['posts']:
        post.comment_list = Comment.objects.filter(post=post)
    
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    info['active'] = 'blog'
    
    return render_to_response('blog/index.html', { 'info': info }, context_instance=RequestContext(request))

def detail(request, post_id):
    info = {}
    
    info['post'] = Post.objects.get(pk=post_id)
    info['comment_list'] = Comment.objects.filter(post=info['post'])
    info['form'] = CommentForm()

    info['links'] = Link.objects.filter(is_public=True)
    
    for c in info['comment_list']:
        if c.author_id:
            u = User.objects.get(pk=c.author_id)
            c.author_name = u.username
            c.author_email = u.email
    
    verses = Verse.objects.filter(is_public=True).order_by('?')
    info['verse'] = verses[0]
    
    info['active'] = 'blog'
    
    return render_to_response('blog/detail.html', { 'info': info }, context_instance=RequestContext(request))

def comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated():
                r = captcha.submit(request.POST['recaptcha_challenge_field'], request.POST['recaptcha_response_field'], settings.RECAPTCHA_PRIVATE_KEY, request.META['REMOTE_ADDR'])
                if not r.is_valid:
                    return redirect('/blog/'+post_id+'/') # Invalid form entry
            f = form.save(commit=False);
          
            f.post_id = post_id
            if request.user.is_authenticated():
                f.author_id = request.user.id
                f.author_name = ''
                f.author_email = ''
            f.save()
        
            email_msg  = 'You have a new comment at http://www.jessicasteiber.com/blog/'+post_id+'/#comments'
            email_from = 'no-reply@jessicasteiber.com'
            email_to   = ['jesi@jessicasteiber.com', 'alan@alanbeam.net']
        
            # Send email notification
            send_mail('New Blog Comment - JessicaSteiber.com', email_msg, email_from, email_to)
        
            return redirect('/blog/'+post_id+'/#comments') # Go back to blog with new comment
        else:
            return redirect('/blog/'+post_id+'/') # Invalid form entry
    else:
        return redirect('/blog/'+post_id+'/') # Go back to blog
