from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=60)
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
        
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
    
class Category(models.Model):
    name = models.CharField(max_length=60)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
        
    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
        
    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
  

    
    