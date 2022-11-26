from django import forms
from django.forms import ModelForm, widgets
from .models import (FollowUp, MedicalHistory, 
                    Pacient, PreprocedureCard, 
                    SurgicalHistory, GastrointestinalProcedure, 
                    UrologicalProcedure, SurgicalProceduralDetail, 
                    RoboticArmLocation, TrocardLocation, BloodLoss, 
                    RobotMalfunction, InstrumentUsed, 
                    AncillaryInstruments, PostProcedural)
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
            "weight":  forms.NumberInput(attrs={"class": "form-control", "style": "width: 100px", "id": "weight"}),                               
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
            "position": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 300px"}),
            "table_height": forms.NumberInput(attrs={"class": "form-control", "style": "width: 100px"}),
            "surg_start_time": widgets.TimeInput(attrs={"class": "form-control", "style": "width: 100px"}),
            "docking_begins": widgets.TimeInput(attrs={"class": "form-control", "style": "width: 100px"}),
            "docking_ends": widgets.TimeInput(attrs={"class": "form-control", "style": "width: 100px"}),
            "console_start_time": widgets.TimeInput(attrs={"class": "form-control", "style": "width: 100px"}),
            "console_end_time": widgets.TimeInput(attrs={"class": "form-control", "style": "width: 100px"}),
            "surg_end_time": widgets.TimeInput(attrs={"class": "form-control", "style": "width: 100px"}),
        }

class RoboticArmLocationForm(ModelForm):
    class Meta:
        model = RoboticArmLocation
        fields = "__all__"
        exclude = ("card_id",) 
        widgets = {"arms_number": forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "undergo_situations": forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table11":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table12":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table13":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table14":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table21":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table22":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table23":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table24":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table31":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table32":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table33":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table34":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table41":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table42":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table43":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table44":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    }

class TrocardLocationForm(ModelForm):
    class Meta:
        model = TrocardLocation
        fields = "__all__"
        exclude = ("card_id",)
        widgets = { "table11":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table12":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table13":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table14":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table21":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table22":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table23":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table24":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table31":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table32":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table33":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table34":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table41":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table42":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table43":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "table44":forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "local_anesthesy_used": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 100px",}),
                    "type_dose":  widgets.Textarea(attrs={"class": "form-control",
            "rows": 2}),
                    }

class BloodLossForm(ModelForm):
    class Meta:
        model = BloodLoss
        fields = "__all__"
        exclude = ("card_id",)
        widgets = { "blood_loss" :forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "undergo_conversion_lap": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 100px",}),
                    "conversion_reason_lap": widgets.Textarea(attrs={"class": "form-control",
                    "rows": 2, "id": "crl"}),
                    "undergo_conversion_open": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 100px",}),
                    "conversion_reason_open": widgets.Textarea(attrs={"class": "form-control",
                    "rows": 2}),
                    "temporary_conversion": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 100px",}),
                    "end_by_robot": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 100px",}),

        }

class RobotMalfunctionForm(ModelForm):
    class Meta:
        model = RobotMalfunction
        fields = "__all__"
        exclude = ("card_id",)
        widgets = {"malfunction": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 300px",}),
                    "comment": widgets.Textarea(attrs={"class": "form-control",
                    "rows": 2}),
                    }

class InstrumentsUsedForm(ModelForm):
    class Meta:
        model = InstrumentUsed
        fields = "__all__"
        exclude = ("card_id",)
        widgets = { "diameter": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 150px",}),
                    "dimension": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 150px",}),
                    "optic_degree": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 150px",}),
                    "manufacturer": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 150px",}),
            
        }

class AncillaryInstrumentsForm(ModelForm):
    class Meta:
        model = AncillaryInstruments
        fields = "__all__"
        exclude = ("card_id",)
        widgets = {"comment": widgets.Textarea(attrs={"class": "form-control",
                    "rows": 2}),}

class PostProceduralForm(ModelForm):
    class Meta:
        model = PostProcedural
        fields = "__all__"
        exclude = ("card_id",)
        widgets = { "brought_ICU": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 150px",}),
                    "start_ICU": widgets.DateInput(attrs={"class": "form-control",
                                                   "type": "date",
                                                   "style": "width: 200px"}),
                    "end_ICU": widgets.DateInput(attrs={"class": "form-control",
                                                   "type": "date",
                                                   "style": "width: 200px"}),
                    "generic_name_l1": forms.TextInput(attrs={"class": "form-control",
                                            "style": "width: 200px"}),
                    "dose_l1": forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "unit_l1": forms.TextInput(attrs={"class": "form-control",
                                            "style": "width: 70px"}),
                    "generic_name_l2": forms.TextInput(attrs={"class": "form-control",
                                            "style": "width: 200px"}),
                    "dose_l2": forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "unit_l2": forms.TextInput(attrs={"class": "form-control",
                                            "style": "width: 70px"}),
                    "generic_name_l3": forms.TextInput(attrs={"class": "form-control",
                                            "style": "width: 200px"}),
                    "dose_l3": forms.NumberInput(attrs={"class": "form-control", "style": "width: 60px"}),
                    "unit_l3": forms.TextInput(attrs={"class": "form-control",
                                            "style": "width: 70px"}),
                    "datetime_discharge": widgets.DateTimeInput(attrs={"class": "form-control",
                                                   "type": "datetime-local",
                                                   "style": "width: 200px"}),
                    "adverse_event_noted": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 150px",}),
        }

class FollowUpForm(ModelForm):
    class Meta:
        model = FollowUp
        fields = "__all__"
        exclude = ("card_id",)
        widgets = { "date_followup": widgets.DateInput(attrs={"class": "form-control",
                                                   "type": "date",
                                                   "style": "width: 200px"}),
                    "any_AE": forms.Select(attrs={"class": "form-select",
                                            "style": "width: 150px",}),}