import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now

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

class PreprocedureCard(models.Model):
    SMOKE_CHOICES = (
        ("Да","Да"),
        ("Нет","Нет"),
    )
    card_id = models.AutoField(primary_key=True)
    pacient_id = models.ForeignKey(
        Pacient,
        on_delete=models.CASCADE,
    )
    creation_date = models.DateTimeField(default=now)
    admission_date = models.DateTimeField(default=now)
    sign_date = models.DateField(default=now)
    is_smoker = models.CharField(max_length=3, choices=SMOKE_CHOICES, default="Нет")
    packyears = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pacient_id)+", "+self.admission_date.date().strftime(r"%d/%m/%Y")
    
    def get_id(self):
        return int(self.card_id)
