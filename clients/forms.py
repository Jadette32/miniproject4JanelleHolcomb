# Author: Janelle Holcomb
# Class: INF 601 Mini Project 4
# Project: Creative Systems Support

from django import forms
from .models import Lead, CallLog, Win
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["business_name", "contact_name", "phone", "email", "address", "source", "notes"]

class CallLogForm(forms.ModelForm):
    class Meta:
        model = CallLog
        fields = ["who", "outcome", "details"]

class WinForm(forms.ModelForm):
    class Meta:
        model = Win
        fields = ["title"]

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
