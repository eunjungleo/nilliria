from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.TextField() # load directly from youtube API
    url_youtube = models.URLField()
    description = models.TextField()
    origins = models.CharField(max_length=10) # country

    def __str__(self):
        return print(self.title + self.origin)
    
    