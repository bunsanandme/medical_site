import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone 

YESNO_CHOICES = (
        ("Да","Да"),
        ("Нет","Нет"),
    )

class Pacient(models.Model):
    GENDER_CHOICES = (
        ("м","Мужчина"),
        ("ж","Женщина"),
    )
    pacient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    date_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=" ")

    def get_id(self):
        return int(self.pacient_id)

    def get_current_age(self):
        import datetime
        age = datetime.datetime.now().year - int(self.date_birth.year)
        count = age % 100
        if count >= 5 and count <= 20:
            age_string = str(age) + ' лет'
        else:
            count = count % 10
            if count == 1:
                age_string = str(age) + ' год'
            elif count >= 2 and count <= 4:
                age_string = str(age) + ' года'
            else:
                age_string = str(age) + ' лет'
        return age_string

    def __str__(self):
        return f"{self.name} {self.surname}"

class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    pacient_id = models.ForeignKey(
        Pacient,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Card #{self.card_id}"

    def get_id(self):
        return self.card_id

class PreprocedureCard(models.Model):
    preprocedure_card_id = models.AutoField(primary_key=True)
    card_id = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        default=0
    )
    creation_date = models.DateTimeField(default=timezone.now())
    admission_date = models.DateTimeField(default=timezone.now())
    sign_date = models.DateField(default=timezone.now())
    is_smoker = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")
    packyears = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return str(self.card_id)+", "+self.admission_date.date().strftime(r"%d/%m/%Y")
    
    def get_id(self):
        return int(self.preprocedure_card_id)

class MedicalHistory(models.Model):
    history_card_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )

    relevant_disease = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")
    has_diabetes = models.BooleanField(default=False)
    has_hypertension = models.BooleanField(default=False)
    has_cardiovascular = models.BooleanField(default=False)
    has_cord = models.BooleanField(default=False)
    has_renal_disease = models.BooleanField(default=False)
    has_liver_disease = models.BooleanField(default=False)
    has_sleep_aphea = models.BooleanField(default=False)
    has_gerd = models.BooleanField(default=False)
    has_depression = models.BooleanField(default=False)
    has_osteoarthritis = models.BooleanField(default=False)
    has_chronic_pain = models.BooleanField(default=False)
    has_stroke = models.BooleanField(default=False)

    def __str__(self):
        return f"MH #{self.history_card_id}"

class SurgicalHistory(models.Model):
    surgical_history_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )
    has_abdominal_surgery = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")
    surgion_description = models.TextField(default="")


    def __str__(self):
        return f"SH #{self.surgical_history_id}"