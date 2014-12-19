from django.db import models

class Link(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title
    
    def get_link(self):
        return '<a href="http://'+self.url+'" alt="'+self.short_description+'" title="'+self.short_description+'" target="_blank">'+self.title+'</a>'
