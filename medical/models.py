import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
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

class GastrointestinalProcedure(models.Model):
    gastro_procedure_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )

    first_surgeon = models.CharField(max_length=40, default=" ", blank=True)
    second_surgeon = models.CharField(max_length=40, default=" ", blank=True)

    cholecystectomy = models.CharField(max_length=80, default=" ", blank=True)
    bariatric = models.CharField(max_length=80, default=" ", blank=True)
    esophageal = models.CharField(max_length=80, default=" ", blank=True)
    gastric = models.CharField(max_length=80, default=" ", blank=True)
    hemicolectomy = models.CharField(max_length=80, default=" ", blank=True)
    liver_surgery = models.CharField(max_length=80, default=" ", blank=True)
    hernia_unilateral = models.CharField(max_length=80, default=" ", blank=True)
    hernia_bilateral = models.CharField(max_length=80, default=" ", blank=True)
    ventral_hernia = models.CharField(max_length=80, default=" ", blank=True)
    fundoplication = models.CharField(max_length=80, default=" ", blank=True)
    sigmoid_resection = models.CharField(max_length=80, default=" ", blank=True)
    rectal = models.CharField(max_length=80, default=" ", blank=True)
    esophagus_implants = models.CharField(max_length=80, default=" ", blank=True)
    linx_implants = models.CharField(max_length=80, default=" ", blank=True)
    other = models.CharField(max_length=200, default=" ", blank=True)

    indication_for_procedure = models.TextField(default=" ", blank=True)
    procedural_details = models.TextField(default=" ", blank=True)
    specification = models.TextField(default=" ", blank=True)
    special_conditions_present = models.TextField(default=" ", blank=True)

    def __str__(self):
        return f"GP #{self.gastro_procedure_id}"

class UrologicalProcedure(models.Model):
    uro_procedure_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )

    first_surgeon = models.CharField(max_length=40, default=" ", blank=True)
    second_surgeon = models.CharField(max_length=40, default=" ", blank=True)

    radical_prostatectomy = models.CharField(max_length=200, default=" ", blank=True)
    lymph_dissection = models.CharField(max_length=200, default=" ", blank=True)
    adrenalectomy = models.CharField(max_length=200, default=" ", blank=True)
    simple_prostatectomy = models.CharField(max_length=200, default=" ", blank=True)
    partial_nephrectomy = models.CharField(max_length=200, default=" ", blank=True)
    radical_nephrectomy = models.CharField(max_length=200, default=" ", blank=True)
    radical_cystectomy  = models.CharField(max_length=200, default=" ", blank=True) 
    ureter_reimplant  = models.CharField(max_length=200, default=" ", blank=True)
    pyeloplasty_UPJ = models.CharField(max_length=200, default=" ", blank=True)
    other = models.CharField(max_length=200, default=" ", blank=True)

    indication_for_procedure = models.TextField(default=" ", blank=True)
    procedural_details = models.TextField(default=" ", blank=True)
    specification = models.TextField(default=" ", blank=True)
    special_conditions_present = models.TextField(default=" ", blank=True)

    def __str__(self):
        return f"UP #{self.uro_procedure_id}"

class SurgicalProceduralDetail(models.Model):
    POSITION_CHOICES = (
        ("Положение лежа на спине", "Положение лежа на спине"),
        ("Положения лежа на животе", "Положения лежа на животе"),
        ("Боковое положение", "Боковое положение"),
        ("Положение с согнутыми ногами","Положение с согнутыми ногами"),
        ("Положение шезлонга", "Положение шезлонга")
    )
    surg_proc_detail_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )

    surg_start_time = models.TimeField(default=timezone.now())
    docking_begins = models.TimeField(default=timezone.now())
    docking_ends = models.TimeField(default=timezone.now())
    console_start_time = models.TimeField(default=timezone.now())
    console_end_time = models.TimeField(default=timezone.now())
    surg_end_time = models.TimeField(default=timezone.now())

    table_height = models.IntegerField(default=0)

    position = models.CharField(max_length=80, choices=POSITION_CHOICES, default="Положение лежа на спине",blank=True)

    indication_for_procedure = models.TextField(default=" ", blank=True)
    procedural_details = models.TextField(default=" ", blank=True)
    specification = models.TextField(default=" ", blank=True)
    special_conditions_present = models.TextField(default=" ", blank=True)

    def __str__(self):
        return f"SPD #{self.surg_proc_detail_id}"

class RoboticArmLocation(models.Model):
    robotic_arm_loc_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )

    arms_number = models.IntegerField(default=0)
    undergo_situations = models.IntegerField(default=0)

    table11 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table12 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table13 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table14 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])

    table21 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table22 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table23 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table24 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])

    table31 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table32 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table33 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table34 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])

    table41 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table42 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table43 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)])
    table44 = models.IntegerField(default=12, validators=[MinValueValidator(1), MaxValueValidator(12)]) 

    def __str__(self):
        return f"RAL #{self.robotic_arm_loc_id}"