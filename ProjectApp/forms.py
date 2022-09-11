


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from ProjectApp.models import  Band, Contact, UserProfile,Photo
class UserProfilForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = '__all__' 
        exclude = ['user','photo']
        widgets = {
            'first_name': forms.Textarea(attrs={'class' : 'fn'}),
            'last_name': forms.Textarea(attrs={'class' : 'ln'}),
            # 'city': forms.Textarea(attrs={'class' : 'city'}),
            'born_date': forms.DateTimeInput(attrs={'type' : 'date', 'class':'date'}),
            'email': forms.EmailInput(attrs={'class' : 'mail'}),
            'phone_number': forms.NumberInput(attrs={'class' : 'phone'}),
            'age':forms.NumberInput(attrs={'class' : 'age'}),
            'country':forms.Textarea(attrs={'class' : 'countries'}),
            

        }
class photoForm(forms.ModelForm):
  
    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ['users']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'first_name': forms.Textarea(attrs={'class' : 'firstcontact'}),
            'last_name': forms.Textarea(attrs={'class' : 'lastcontact'}),
            'email': forms.EmailInput(attrs={'class' : 'mailcontact'}),
            'phone_number': forms.NumberInput(attrs={'class' : 'phonecontact'}),
            'subject':forms.Textarea(attrs={'class' : 'subject'}),
            'message':forms.Textarea(attrs={'class' : 'message'}),
            

        }
# class SearchForm(forms.ModelForm):
#     class Meta:
#         model = Search
#         fields= '__all__'
#         widgets = {
#              'city': forms.Textarea(attrs={'class' : 'city'}),

#         }
class CreateBandForm(forms.ModelForm):
    class Meta:
        model= Band
        fields ='__all__'
        exclude= ['members']

class AddToBandForm(forms.Form):
    # def __init__(self, user, *args, **kwargs):
    #     super(AddToBandForm, self).__init__(*args, **kwargs)
        # self.fields.band.queryset = user.userprofile.bands.all()
    band = forms.ModelMultipleChoiceField(queryset=Band.objects.all())
    new_member = forms.ModelChoiceField(queryset=UserProfile.objects.all())