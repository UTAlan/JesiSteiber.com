from django.db import models

class Verse(models.Model):
    reference = models.CharField(max_length=255)
    verse = models.TextField()
    is_public = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.reference
