from django import forms
from .models import Feedmain



class Feedmainform(forms.ModelForm):
    class Meta:
        model=Feedmain
        fields=['rating']

