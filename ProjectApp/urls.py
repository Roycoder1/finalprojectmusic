

from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView

from ProjectApp.views import  add_to_band, bands, create_band, results,contact, get_queryset, register,homepage,add_data,profile,hotel_image_view, results,success


urlpatterns = [
   
    path("" , LoginView.as_view(), name='login'),
    path("register" , register , name='register'),
    path("home", homepage,name= 'home' ),
    path("logout",LogoutView.as_view(template_name = 'logout.html'),name='logout'),
    path("personaldata",add_data,name='data'),
    path("profile", profile , name='profile'),
    # path("edit/<int:id>", edit_picture, name='edit'),
    path('image_upload', hotel_image_view, name = 'image_upload'),
    path('success', success, name = 'success'),
    path('contact', contact, name='contact'),
    path('musicians',get_queryset, name='musicians'),
    path('results', results, name='results'),
    path('bands',bands , name='bands'),
    path('createbands',create_band, name='createbands'),
    path('add_members/<int:id>' , add_to_band , name='add_members')
    

]