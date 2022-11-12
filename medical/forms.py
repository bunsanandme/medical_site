from django import forms
from django.forms import ModelForm, widgets
from .models import Pacient

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class PacientForm(ModelForm):
    class Meta:
        model = Pacient
        fields = ("name", "surname", "gender", "date_birth")
        widgets = {
            "gender": forms.Select(attrs={"class": "form-select",
                                          "style": "width: 200px"}),
            'date_birth': widgets.DateInput(attrs={'type': 'date',
                                                   "style": "width: 200px"})
        }

class SearchForm(forms.Form):
    search_input = forms.CharField(widget=forms.TextInput(attrs={"type":"text", 
    "class":"form-control", 
    "placeholder": "Найти пациента...",
    "aria-label":"Найти пациента",
    "aria-describedby":"basic-addon2"}))
