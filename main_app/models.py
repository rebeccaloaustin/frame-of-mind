from django.db import models
from django.urls import reverse

class Artist(models.Model): 
    image = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    about = models.TextField(null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('artists_detail', kwargs={'artist_id': self.id})
class Art(models.Model): 
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('artworks_detail', kwargs={'art_id': self.id})
    


