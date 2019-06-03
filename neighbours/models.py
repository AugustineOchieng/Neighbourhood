from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# from .forms import NewPersonForm, BusinessForm

class Neighbourhood(models.Model):
  neighbourhood_name = models.CharField(max_length=30)
  neighbourhood_location = models.CharField(max_length=30)
  occupants_count = models.IntegerField(default=0,validators=[MaxValueValidator(1000)])
# Admin Foreign key
  def __str__(self):
        return self.neighbourhood_name

class Person(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  neighbourhood = models.ForeignKey(Neighbourhood)
  email_address = models.CharField(max_length=30)
  profile_picture = models.ImageField(upload_to='profiel_pic/')
  bio = models.CharField(max_length=100)

  def __str__(self):
        return self.bio

class Business(models.Model):
  business_name = models.CharField(max_length=30)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='replicate')
  neighbourhood = models.ForeignKey(Neighbourhood)
  business_email_address = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  def __str__(self):
        return self.business_name

class Post(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'studio/', default="")
    person = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    
    def __str__(self):
        return self.image_name
