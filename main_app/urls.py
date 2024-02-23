from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('addto/', views.addto, name='addto'),
 path('artworks/', views.artworks_index, name='artworks_index'),
 path('artworks/<int:art_id>/', views.artworks_detail, name="artworks_detail"),
 path('artworks/create/', views.ArtCreate.as_view(), name="artworks_create"),
 path('artworks/<int:pk>/update/', views.ArtUpdate.as_view(), name='artworks_update'),
 path('artworks/<int:pk>/delete/', views.ArtDelete.as_view(), name='artworks_delete'),
 path('artists/', views.artists_index, name='artists_index'),
 path('artists/<int:artist_id>/', views.artists_detail, name="artists_detail"),
 path('artists/create/', views.ArtistCreate.as_view(), name="artists_create"),
 path('artists/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artists_update'),
 path('artists/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artists_delete'),
]