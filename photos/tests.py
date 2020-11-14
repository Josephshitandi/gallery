from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(id=1,name = 'Nairobi')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))
        
    # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location)== 0)        

        
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category = Category(id=1,name = 'Travel')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))
        
    # Testing Save Method
    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
        
    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category)== 0)
        
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new location and saving it
        self.location = Location(id=1,name = 'Nairobi')
        self.location.save_location()

        # Creating a new category and saving it
        self.category = Category(id=1,name = 'Travel')
        self.category.save_category()

        self.new_image= Image(id=1, name='image', description='this is a test image', location=self.location,category=self.category)
        self.new_image.save()

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    # def tearDown(self):
    #     Location.objects.all().delete()
    #     Category.objects.all().delete()
    #     Image.objects.all().delete()