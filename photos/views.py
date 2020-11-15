from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Location,Category

# Create your views here.
def my_gallery(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'gallery.html', {"date": date,"images":images})
