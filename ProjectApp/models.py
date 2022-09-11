from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.
class Photo(models.Model):
    profile_pic = models.ImageField(upload_to='images/',null=True, blank=True)

class City(models.Model):
    
    city = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.city)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField( null=True, blank=True)
    born_date= models.DateField( null=True, blank=True)
    age = models.IntegerField( null=True, blank=True)
    phone_number = models.IntegerField( null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE , null=True)
    countries = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    photo = models.OneToOneField(Photo, on_delete=models.CASCADE,null=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} { self.last_name}'
    # def get_absolute_url(self):
    #     return reverse('profile', args = [self.id])
    

def post_profile_group(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.is_staff:
            userprofile=UserProfile.objects.create(user_id = instance.id)
            new_photo = Photo.objects.create()
            userprofile.photo = new_photo
            userprofile.save()
post_save.connect(receiver=post_profile_group, sender=User)

class Contact(models.Model):
    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    phone_number = models.IntegerField( null=True, blank=True)
    email = models.EmailField( null=True, blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=499)

class Band(models.Model):
    name = models.CharField(max_length=140)
    members = models.ManyToManyField(UserProfile,related_name='bands')

    def __str__(self) -> str:
        return self.name

