from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt

# Create your views here.
def my_gallery(request):
    date = dt.date.today()
    return render(request, 'gallery.html', {"date": date})
