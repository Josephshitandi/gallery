from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Location,Category

# Create your views here.
def my_gallery(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'gallery.html', {"date": date,"images":images})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_images = Image.search_by_category(category)
        # searched_images = Image.filter_by_location(category)
        message = f"{category}"
        return render(request, 'search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {"message": message})
    
def search_location(request):
    if 'location' in request.GET and request.GET["location"]:
        location = request.GET.get("location")
        searched_images = Image.filter_by_location(location)
        message = f"{location}"
        print("Image.......",searched_images)
        return render(request, 'location.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image lacation"
        return render(request, 'location.html', {"message": message})
