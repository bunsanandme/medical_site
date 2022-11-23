from django import forms
from django.forms import ModelForm, widgets
from .models import MedicalHistory, Pacient, PreprocedureCard, SurgicalHistory, GastrointestinalProcedure, UrologicalProcedure, SurgicalProceduralDetail, RoboticArmLocation, TrocardLocation, BloodLoss, RobotMalfunction, InstrumentUsed
from datetime import datetime
from zoneinfo import ZoneInfo
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
            'date_birth': widgets.DateInput(attrs={"class": "form-control",
                                                    'type': 'date',
                                                   "style": "width: 200px"}),
            "name": forms.TextInput(attrs={"class": "form-control",
                                            "style": "width: 300px"}),
            "surname": forms.TextInput(attrs={"class": "form-control",
                                            "style": "width: 300px"}),
        }

    def clean_date_birth(self):
        date_birth = self.cleaned_data['date_birth']
        print(type(date_birth))
        if date_birth >= datetime.now().date():
            raise forms.ValidationError('Дата рождения не может быть позже сегодняшней даты')
        return date_birth

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
            'creation_date': widgets.DateInput(attrs={"class": "form-control",
                                                   "type": "date",
                                                   "style": "width: 200px",
                                                   "required": True}),
            'admission_date': widgets.DateTimeInput(attrs={"class": "form-control",
                                                   "type": "datetime-local",
                                                   "style": "width: 200px"}),
            'sign_date': widgets.DateInput(attrs={"class": "form-control",
                                                   "type": "date",
                                                   "style": "width: 200px"}),
            "is_smoker":   forms.Select(attrs={"class": "form-select",
                                            "style": "width: 200px",
                                            "id": "smoker",}),
            "packyears": forms.TextInput(attrs={"class": "form-control",
                                                "id": "packyears",
                                                "style": "width: 100px",}),
            "height":  forms.NumberInput(attrs={"class": "form-control", "style": "width: 100px", "id": "height"}),
            "weight":  forms.NumberInput(attrs={"class": "form-control", "style": "width: 100px",}),                               
            }
    
    def clean_creation_date(self):
        creation_date = self.cleaned_data['creation_date']
        print(type(creation_date))
        if creation_date >= datetime.now(tz=ZoneInfo("Europe/Moscow")):
            raise forms.ValidationError('Дата создания записи не может быть позже сегодняшней даты')
        return creation_date

    def clean_admission_date(self):
        admission_date = self.cleaned_data['admission_date']
        if admission_date >= datetime.now(tz=ZoneInfo("Europe/Moscow")):
            raise forms.ValidationError('Дата приема записи не может быть позже сегодняшней даты')
        return admission_date

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

class RoboticArmLocationForm(ModelForm):
    class Meta:
        model = RoboticArmLocation
        fields = "__all__"
        exclude = ("card_id",)

class TrocardLocationForm(ModelForm):
    class Meta:
        model = TrocardLocation
        fields = "__all__"
        exclude = ("card_id",)

class BloodLossForm(ModelForm):
    class Meta:
        model = BloodLoss
        fields = "__all__"
        exclude = ("card_id",)

class RobotMalfunctionForm(ModelForm):
    class Meta:
        model = RobotMalfunction
        fields = "__all__"
        exclude = ("card_id",)

class InstrumentsUsedForm(ModelForm):
    class Meta:
        model = InstrumentUsed
        fields = "__all__"
        exclude = ("card_id",)
