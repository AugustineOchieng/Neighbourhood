from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Neighbourhood, Person, Post, Business
from django.contrib.auth.decorators import login_required
from .forms import NewPersonForm, BusinessForm, NeighbourhoodForm
  
# Create your views here.
def index(request):

    
    make = Neighbourhood.objects.all()
    # images = Image.objects.get(id = image_id)
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'neighbourhoods': make,"posts": posts})



@login_required(login_url='/accounts/login/')
def home(request):

    
    return render(request, 'home.html')
  

# def user(request):  
#     contextual = {
#     'users': User.objects.all()
#     }
# return render(request, 'index.html', contextual)
@login_required(login_url='/accounts/login/')
def person(request, id):
    current_user = request.user
    # images = Image.objects.filter(profile = current_user)

    try:
        users = Person.objects.filter(user=id)
    except ObjectDoesNotExist:
        return redirect('new_user_profile')

    return render(request, 'user_profile.html', {'users': users, 'current_user': current_user})

@login_required(login_url='/accounts/login/')     
def new_person(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPersonForm(request.POST, request.FILES)
        if form.is_valid():
            person = form.save(commit=False)
            person.user = current_user
            person.userId = request.user.id
            person.save()
        return redirect('index')

    else:
        form = NewPersonForm()
        return render(request, 'new_user_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')  
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user = Person.objects.filter(user=request.user).first()
        form = NewPersonForm(request.POST, request.FILES, instance=user)
        person = Person.objects.filter(user_id =current_user.id)
        if form.is_valid():
            form.save()
        return redirect('edit_profile')
    else:
        form = NewPersonForm()
    return render(request, 'home.html', {'form': form})

def search_results(request):

     if 'business' in request.GET and request.GET ["business"]:
         search_term = request.GET.get("business")
         searched_profiles = Profile.search_by_username(search_term)
         message = f"{search_term}"

         return render(request, 'search.html', {"message":message, "bliss":searched_bliss})
     else:
         message = "You haven't seached for any users yet!"
         return render(request, 'search.html', {"message": message})
         
@login_required(login_url='/accounts/login/')
def work(request):
  

    try:
        businesses = Business.objects.all()
    except ObjectDoesNotExist:
        return redirect('work')

    return render(request, 'business.html', {'businesses': businesses})
    
@login_required(login_url='/accounts/login/')  
def moving(request):
    current_user = request.user
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.profile = current_user
            # project.poster_id = current_user.id
            neighbourhood.save()
        return redirect('index')

    else:
        form = NeighbourhoodForm()
    return render(request, 'new_neighbourhood.html', {"form": form})