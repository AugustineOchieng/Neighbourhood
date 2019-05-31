from django.shortcuts import render, redirect
from .models import Neighbourhood


  
# Create your views here.
def index(request):

    
    make= Neighbourhood.objects.all()
    
    return render(request, 'index.html', {'neighbourhoods': make})
  
def home(request):

    
    return render(request, 'home.html')
  

# def user(request):
#     contextual = {
#     'users': User.objects.all()
#     }
#     return render(request, 'index.html', contextual)