from dataclasses import field
from pyexpat import model
from tkinter import Widget
from turtle import textinput
from django.forms import ModelForm, TextInput
from .models import City

class cityform(ModelForm):
    class Meta:
        model=City
        fields=['name']
        widgets={'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City name'})}