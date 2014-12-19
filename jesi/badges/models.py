from django.db import models

class Badge(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title
