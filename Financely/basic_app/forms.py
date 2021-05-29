from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Stock



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

# class updateQuantityForm(forms.ModelForm):
#     class Meta:
#         model = Stock
#         fields = ['quantity']
