from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Art
from .models import Artist

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def addto(request):
    return render(request, 'addto.html')
def artworks_index(request):
  artworks = Art.objects.all()
  return render(request, 'artworks/artworks_index.html', { 'artworks': artworks })
def artworks_detail(request, art_id):
    art = Art.objects.get(id=art_id)
    return render(request, 'artworks/artworks_detail.html', { 'art': art })
class ArtCreate(CreateView):
    model = Art
    fields = '__all__'
    success_url = '/artworks/'
class ArtUpdate(UpdateView):
  model = Art
  fields = ['name', 'image','description']

class ArtDelete(DeleteView):
  model = Art
  success_url = '/artworks/'

def artists_index(request):
  artists = Artist.objects.all()
  return render(request, 'artists/artists_index.html', { 'artists': artists })
def artists_detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    artworks = artist.art_set.all()
    return render(request, 'artists/artists_detail.html', {'artist': artist, 'artworks': artworks})
class ArtistCreate(CreateView):
    model = Artist
    fields = '__all__'
    success_url = '/artists/'
class ArtistUpdate(UpdateView):
  model = Artist
  fields = ['name', 'about', 'image']

class ArtistDelete(DeleteView):
  model = Artist
  success_url = '/artists/'

