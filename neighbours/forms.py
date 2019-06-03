from django import forms
from .models import  Person, Business, Neighbourhood



   
class NewPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['user']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighbourhood']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['user', 'email_address', 'profile_picture', 'bio']