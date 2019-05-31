from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Neighbourhood(models.Model):
  neighbourhood_name = models.CharField(max_length=30)
  neighbourhood_location = models.CharField(max_length=30)
  occupants_count = models.IntegerField(default=0,validators=[MaxValueValidator(1000)])
# Admin Foreign key
  def __str__(self):
        return self.neighbourhood_name

class User(models.Model):
  name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  neighbourhood = models.ForeignKey(Neighbourhood)
  email_address = models.CharField(max_length=50)

class Business(models.Model):
  business_name = models.CharField(max_length=30)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='replicate')
  neighbourhood = models.ForeignKey(Neighbourhood)
  business_email_address = models.CharField(max_length=50)

