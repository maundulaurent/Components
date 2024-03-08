from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# create user
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username','password1','password2']

# login user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# create record
class CreateRecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'county', 'country']


# update a record 
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'county', 'country']



# class ClearanceTestForm(forms):
#     name = forms.CharField(max_length=200),
#     reg_no = forms.CharField(),
#     year_of_study = forms.IntegerField()