from django import forms
from django.forms import ModelForm
from .models import Anime_Model


class Anime_Form(forms.ModelForm):
    class Meta:
        model = Anime_Model
        fields = '__all__'
