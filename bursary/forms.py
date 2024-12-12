from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user', 'Constituency', 'year_of_study','fees_structure','institution']


class ApplicationForm(ModelForm):
    class Meta:
        model = Applications
        fields = '__all__'
        exclude = ['student','date_created']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

