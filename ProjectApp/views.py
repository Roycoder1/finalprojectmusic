from ast import Return
from distutils import errors
from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404

from .models import Band, City, UserProfile,Band
from ProjectApp.models import Photo
from django.contrib.auth.models import User
from .forms import ContactForm, CreateBandForm, UserProfilForm,photoForm,AddToBandForm
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.

class AdminLogin(LoginView):
    template_name = 'login.html'
    
    



def register(request):
    context = {'form': UserCreationForm}
    if request.method == 'POST':
        
        form_filled = UserCreationForm(request.POST)

        if form_filled.is_valid():

            form_filled.save()
            
            u_username = form_filled.cleaned_data['username']
            u_password = form_filled.cleaned_data['password1']
           
            user = authenticate(username = u_username, password = u_password)

            if user :
                login(request, user)
                return redirect('data')
            else:
                print("User not authenticated")
        
        else:

            return render(request, 'register.html', {'form': form_filled})

    return render(request, 'register.html', context)

def add_data(request):
    profile = request.user.userprofile
    form = UserProfilForm(request.POST or None, instance=profile)
    # form_search = SearchForm(request.POST or None)

    context = {'form': form }

    if form.is_valid():
        userprofile=form.save()
        
        # print(userprofile.photo)

        
        return redirect('login')
    else:
        print(form.errors)
        
    
    return render(request, 'store.html', context)

def homepage(request):
    return render (request, 'home.html')

def profile(request):
    user = request.user
    
    profile = user.userprofile 

    context = {'profile': profile}
    if user.userprofile.photo:

        profile_picture = user.userprofile.photo
        context={'profile':profile, 'profile_picture': profile_picture}
    #     print(profile_picture)
    
    # print(profile)  
    
    
    

    return render(request, 'profile.html', context)

def hotel_image_view(request):
    print(request.user.userprofile.photo)
    if request.method == 'POST':
        form = photoForm(request.POST, request.FILES,instance=request.user.userprofile.photo)
  
        if form.is_valid():
            form.save()
            # print(request.user.userprofile.photo)

            return redirect('success')
            
    else:
        form = photoForm()
    return render(request, 'photo.html', {'form' : form})
  
  
def success(request):
    return redirect('profile')

# def edit_picture(request,id):
#     users = Photo.objects.get(id=id)
#     print(users)
#     form = photoForm(request.FILES,instance=users)
#     if request.method =='POST':
#         form = photoForm(request.POST, request.FILES, instance=users)
#         form.save()
#         return redirect('profile')
#     return render(request, 'photo.html', {'form' : form})


def contact (request):
    context = {'form': ContactForm}
    if request.method == 'POST':

        date = ContactForm(request.POST)

        if date.is_valid():
            date.save()
            return redirect('home')
            
    return render(request, 'contact.html', context)
# def profile_view(request):
#     photos = UserProfile.objects.photo

#     photo_media = ""
    
    
#     context = {'photos': photos}
#     return render(request, 'animes.html', context)

# def find_musicians(request):
#     allprofile = UserProfile.objects.all()

def results(request):
    # Query all posts
    search_post = request.POST.get('searchcity')
    
    

    if search_post:
        print(search_post)
        find_city = City.objects.filter(city__contains= search_post)
        # print(find_city[0])
        posts = UserProfile.objects.filter(Q(city=find_city[0]))
        # print('friend')
        # return posts
    else:
        posts = UserProfile.objects.all().order_by("-born_date")
        # print('hi')
    
    return render(request, 'results.html', {'posts': posts})
    # book = get_object_or_404(UserProfile, id=id)

    # types = UserProfile.objects.all()

    # t = types.get(id=book.type.id)

    # return render(request, 'results.html', {'book': book, 'type': t.btype})



    
def get_queryset(request):  # new
    search_post = request.POST.get('searchcity')
    print(type(search_post))
    # if search_post:
    #     posts = UserProfile.objects.filter(Q(city__icontains=search_post))
    #     print('friend')
    #     # return posts
    # else:
    #     posts = UserProfile.objects.all().order_by("-born_date")
    #     print('hi')
        
    # context = {'info':allprofile}
    return render(request, 'musicians.html')


def bands(request):
    # group_user = request.user
    # group_unique = UserProfile.objects.get(email=group_user)
    
    bands_user = request.user.userprofile.bands.all()
    print(bands_user)
    
    



    return render(request , 'bands.html',{'bands':bands_user})

def create_band(request):
    form = CreateBandForm(initial={"members": [request.user]})
    if request.method == 'POST':
        form_filled = CreateBandForm(request.POST)
        
        if form_filled.is_valid():
            band = form_filled.save()
            band.members.add(request.user.userprofile)
            band.save()
    
            return redirect('bands')
    return render(request, 'create_bands.html',{'form':form})

def add_to_band(request,id):
    
    userprofile = request.user.userprofile
    print(userprofile)
    profile = UserProfile.objects.get(id=id)
    print(id)
    print(profile)
    form = AddToBandForm(initial = {'bands': userprofile.bands.all(), 'new_member': profile})

    if request.method == 'POST':
        form = AddToBandForm(request.POST)

        

        if form.is_valid():
            band = form.cleaned_data['band']
            new_member = form.cleaned_data['new_member']
            new_member.bands.add(*band)
            
            return render(request , 'bands.html',{'member':new_member})
    # band = Band.objects.get(id=id)
    # print(band)
    # we have the id of the user when we click on the buttom
    # next step when we press on the button choose we need to get the id of the group
    #then display users int
    


    # form = AddToBandForm(initial = {'bands': userprofile.bands.all(), 'new_member': profile})
       # form = AddToBandForm(initial={'bands':[request.user]})
    # profile_band1 = Band.objects.filter(Q(id=user))
    # profile_band = UserProfile.objects.filter(Q(id=profile))
    return render(request, 'add_members.html', {'form':form , 'profile':profile})
