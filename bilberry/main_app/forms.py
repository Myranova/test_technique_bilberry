from django import forms

class PhotoForm(forms.Form):
    nom = forms.CharField()
    photo = forms.ImageField()