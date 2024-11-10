from django.http import HttpResponse
from django.shortcuts import render
from .models import Photo

def index(request):
  photos = Photo.objects.all()
  return render(request, 'photos/index.html', {'photos': photos, 'main_photo':photos.first})