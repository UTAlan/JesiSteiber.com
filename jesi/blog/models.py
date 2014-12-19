from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group

class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return settings.SITE_URL + 'blog/' + str(self.id) + '/'

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User, blank=True, null=True)
    author_name = models.CharField(max_length=200, null=True)
    author_email = models.EmailField(null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        result = ''
        if self.author:
            result = self.author.username
        else:
            result = self.author_name
        return result + ': ' + self.content
