from django import forms
from django.forms import ModelForm, widgets
from .models import MedicalHistory, Pacient, PreprocedureCard, SurgicalHistory, GastrointestinalProcedure, UrologicalProcedure, SurgicalProceduralDetail

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

class PreprocedureCardForm(ModelForm):
    class Meta:
        model = PreprocedureCard
        fields = ("creation_date", "admission_date", "sign_date", "is_smoker", "packyears", "height", "weight")
        widgets = {
            'admission_date': widgets.DateTimeInput(attrs={"type": "datetime-local",
                                                   "style": "width: 220px"}),
            'sign_date': widgets.DateInput(attrs={"type": "date",
                                                   "style": "width: 200px"}),
            "is_smoker":   forms.Select(attrs={"class": "form-select",
                                            "style": "width: 200px",
                                            "id": "smoker",}),                               
            "packyears": forms.TextInput(attrs={"id": "packyears",})                                       
            }

class MedicalHistoryForm(ModelForm):
    class Meta:
        model = MedicalHistory
        fields = "__all__"
        exclude = ("card_id",)
        widgets = {"relevant_disease": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 100px",})}

class SurgicalHistoryForm(ModelForm):
    class Meta:
        model = SurgicalHistory
        fields = "__all__"
        exclude = ("card_id",)
        widgets = {"surgion_description": widgets.Textarea(attrs={"class": "form-control",
                                                                  "id": "surgion_description"}),
                   "has_abdominal_surgery": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 100px",})}
                        
class GastrointestinalProcedureForm(ModelForm):
    class Meta:
        model = GastrointestinalProcedure
        fields = "__all__"
        exclude = ("card_id",)
        widgets = {"indication_for_procedure": widgets.Textarea(attrs={"class": "form-control",
                                                                "rows": 2}),
                    "procedural_details": widgets.Textarea(attrs={"class": "form-control",
                                                                   "rows": 2}),
                    "specification": widgets.Textarea(attrs={"class": "form-control",
                    "rows": 2}),
                    "special_conditions_present": widgets.Textarea(attrs={"class": "form-control",
                    "rows": 2}),
                    
        }

class UrologicalProcedureForm(ModelForm):
    class Meta:
        model = UrologicalProcedure
        fields = "__all__"
        exclude = ("card_id",)
        widgets = {"indication_for_procedure": widgets.Textarea(attrs={"class": "form-control",
                                                                "rows": 2}),
                    "procedural_details": widgets.Textarea(attrs={"class": "form-control",
                                                                   "rows": 2}),
                    "specification": widgets.Textarea(attrs={"class": "form-control",
                    "rows": 2}),
                    "special_conditions_present": widgets.Textarea(attrs={"class": "form-control",
                    "rows": 2}),
                }

class SurgicalProceduralDetailForm(ModelForm):
    class Meta:
        model = SurgicalProceduralDetail
        fields = "__all__"
        exclude = ("card_id",)
        widgets = {"indication_for_procedure": widgets.Textarea(attrs={"class": "form-control",
                                                        "rows": 2}),
            "procedural_details": widgets.Textarea(attrs={"class": "form-control",
                                                            "rows": 2}),
            "specification": widgets.Textarea(attrs={"class": "form-control",
            "rows": 2}),
            "special_conditions_present": widgets.Textarea(attrs={"class": "form-control",
            "rows": 2}),
        }