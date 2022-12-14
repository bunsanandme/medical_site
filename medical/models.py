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
        ("Мужчина","Мужчина"),
        ("Женщина","Женщина"),
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
    height = models.IntegerField(default=0, validators=[MaxValueValidator(300)])
    weight = models.IntegerField(default=0, validators=[MaxValueValidator(300)])

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
    surgion_description = models.TextField(default="", blank=True)


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

    cholecystectomy = models.BooleanField(default=False, blank=True)
    bariatric = models.BooleanField(default=False, blank=True)
    esophageal = models.BooleanField(default=False, blank=True)
    gastric = models.BooleanField(default=False, blank=True)
    hemicolectomy = models.BooleanField(default=False, blank=True)
    liver_surgery = models.BooleanField(default=False, blank=True)
    hernia_unilateral = models.BooleanField(default=False, blank=True)
    hernia_bilateral = models.BooleanField(default=False, blank=True)
    ventral_hernia = models.BooleanField(default=False, blank=True)
    fundoplication = models.BooleanField(default=False, blank=True)
    sigmoid_resection = models.BooleanField(default=False, blank=True)
    rectal = models.BooleanField(default=False, blank=True)
    esophagus_implants = models.BooleanField(default=False, blank=True)
    linx_implants = models.BooleanField(default=False, blank=True)
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

    radical_prostatectomy = models.BooleanField(default=False, blank=True)
    lymph_dissection = models.BooleanField(default=False, blank=True)
    adrenalectomy = models.BooleanField(default=False, blank=True)
    simple_prostatectomy = models.BooleanField(default=False, blank=True)
    partial_nephrectomy = models.BooleanField(default=False, blank=True)
    radical_nephrectomy = models.BooleanField(default=False, blank=True)
    radical_cystectomy  = models.BooleanField(default=False, blank=True)
    ureter_reimplant  = models.BooleanField(default=False, blank=True)
    pyeloplasty_UPJ = models.BooleanField(default=False, blank=True)
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

    position = models.CharField(max_length=80, choices=POSITION_CHOICES, default="Положение лежа на спине")

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

    table11 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table12 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table13 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table14 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)

    table21 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table22 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table23 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table24 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)

    table31 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table32 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table33 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table34 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)

    table41 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table42 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table43 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    table44 = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True) 

    def __str__(self):
        return f"RAL #{self.robotic_arm_loc_id}"

class TrocardLocation(models.Model):
    trocard_location_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )

    table11 = models.CharField(default="", max_length=2, blank=True, null=True)
    table12 = models.CharField(default="", max_length=2, blank=True, null=True)
    table13 = models.CharField(default="", max_length=2, blank=True, null=True)
    table14 = models.CharField(default="", max_length=2, blank=True, null=True)

    table21 = models.CharField(default="", max_length=2, blank=True, null=True)
    table22 = models.CharField(default="", max_length=2, blank=True, null=True)
    table23 = models.CharField(default="", max_length=2, blank=True, null=True)
    table24 = models.CharField(default="", max_length=2, blank=True, null=True)

    table31 = models.CharField(default="", max_length=2, blank=True, null=True)
    table32 = models.CharField(default="", max_length=2, blank=True, null=True)
    table33 = models.CharField(default="", max_length=2, blank=True, null=True)
    table34 = models.CharField(default="", max_length=2, blank=True, null=True)

    table41 = models.CharField(default="", max_length=2, blank=True, null=True)
    table42 = models.CharField(default="", max_length=2, blank=True, null=True)
    table43 = models.CharField(default="", max_length=2, blank=True, null=True)
    table44 = models.CharField(default="", max_length=2, blank=True, null=True) 

    local_anesthesy_used = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")
    type_dose = models.TextField(default=" ", blank=True)

    def __str__(self):
        return f"TL #{self.trocard_location_id}"


class BloodLoss(models.Model):
    blood_loss_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )

    blood_loss = models.IntegerField(default=0, validators=[MaxValueValidator(4500)])
    undergo_conversion_lap = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")
    conversion_reason_lap = models.TextField(default=" ", blank=True)

    undergo_conversion_open = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")
    conversion_reason_open = models.TextField(default=" ", blank=True)

    temporary_conversion = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")

    end_by_robot = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")
    def __str__(self):
        return f"BL #{self.blood_loss_id}"\

class RobotMalfunction(models.Model):
    rob_mal_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
    Card,
    on_delete=models.CASCADE,
    default=0)

    MALFUNCTION_CHOISE = (
        ("Нет", "Нет"),
        ("Неисправность консоли","Неисправность консоли"),
        ("Неисправность монитора/камеры","Неисправность монитора/камеры"),
        ("Ограниченное движение","Ограниченное движение"),
        ("Столкновение","Столкновение"),
        ("Другое","Другое")
    )

    malfunction = models.CharField(max_length=50, default="Нет", choices=MALFUNCTION_CHOISE)
    comment = models.TextField(default=" ", blank=True)
    def __str__(self):
        return f"RB #{self.rob_mal_id}"


class InstrumentUsed(models.Model):
    inst_use_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )

    DIAMETER_CHOICES = (
        ("5mm", "5mm"),
        ("10mm", "10mm")
    )

    DIMENSION_CHOICES = (
        ("2D", "2D"),
        ("3D", "3D"),
        ("4D", "4D"),
    )

    OPTIC_DEGREE_CHOICES = (
        ("0°", "0°"),
        ("30°", "30°")
    )

    MANUFACTURER_CHOICES = (
        ("Conmed","Conmed"),
        ("NovaDAQ", "NovaDAQ"),
        ("Wolf","Wolf"),
        ("Stryker","Stryker"),
        ("Storz","Storz"),
        ("Olympus", "Olympus")
    )

    diameter = models.CharField(max_length=4, default=" ", choices=DIAMETER_CHOICES)
    dimension = models.CharField(max_length=2, default=" ", choices=DIMENSION_CHOICES)
    optic_degree = models.CharField(max_length=10, default=" ", choices= OPTIC_DEGREE_CHOICES)
    manufacturer = models.CharField(max_length=10, default=" ", choices=MANUFACTURER_CHOICES)

    table_pi1_3 = models.BooleanField(default=False, blank=True)
    table_pi2_3 = models.BooleanField(default=False, blank=True, )
    table_pi3_3 = models.BooleanField(default=False, blank=True, )
    table_pi4_3 = models.BooleanField(default=False, blank=True, )

    table_mi1_3 = models.BooleanField(default=False, blank=True, )
    table_mi2_3 = models.BooleanField(default=False, blank=True, )
    table_mi3_3 = models.BooleanField(default=False, blank=True, )

    table_bi1_3 = models.BooleanField(default=False, blank=True, )
    table_bi2_3 = models.BooleanField(default=False, blank=True, )
    
    table_pi1_5 = models.BooleanField(default=False, blank=True, )
    table_pi2_5 = models.BooleanField(default=False, blank=True, )
    table_pi3_5 = models.BooleanField(default=False, blank=True, )
    table_pi4_5 = models.BooleanField(default=False, blank=True, )
    table_pi5_5 = models.BooleanField(default=False, blank=True, )
    table_pi6_5 = models.BooleanField(default=False, blank=True, )
    table_pi7_5 = models.BooleanField(default=False, blank=True, )
    table_pi8_5 = models.BooleanField(default=False, blank=True, )
    table_pi9_5 = models.BooleanField(default=False, blank=True, )
    table_pi10_5 = models.BooleanField(default=False, blank=True, )
    table_pi10_5 = models.BooleanField(default=False, blank=True, )
    table_pi11_5 = models.BooleanField(default=False, blank=True, )
    table_pi12_5 = models.BooleanField(default=False, blank=True, )
    table_pi13_5 = models.BooleanField(default=False, blank=True, )
    table_pi14_5 = models.BooleanField(default=False, blank=True, )
    table_pi15_5 = models.BooleanField(default=False, blank=True, )
    table_pi16_5 = models.BooleanField(default=False, blank=True, )
    table_pi17_5 = models.BooleanField(default=False, blank=True, )

    table_mi1_5 = models.BooleanField(default=False, blank=True, )
    table_mi2_5 = models.BooleanField(default=False, blank=True, )
    table_mi3_5 = models.BooleanField(default=False, blank=True, )
    table_mi4_5 = models.BooleanField(default=False, blank=True, )
    table_mi5_5 = models.BooleanField(default=False, blank=True, )
    table_mi6_5 = models.BooleanField(default=False, blank=True, )
    table_mi7_5 = models.BooleanField(default=False, blank=True, )
    table_mi8_5 = models.BooleanField(default=False, blank=True, )

    table_bi1_5 = models.BooleanField(default=False, blank=True, )
    table_bi2_5 = models.BooleanField(default=False, blank=True, )
    table_bi3_5 = models.BooleanField(default=False, blank=True, )
    table_bi4_5 = models.BooleanField(default=False, blank=True, )
    table_bi5_5 = models.BooleanField(default=False, blank=True, )

    table_pi1_10 = models.BooleanField(default=False, blank=True, )
    table_pi2_10 = models.BooleanField(default=False, blank=True, )

    table_ca1 = models.BooleanField(default=False, blank=True, )
    table_ca2 = models.BooleanField(default=False, blank=True, )
    table_ca3 = models.BooleanField(default=False, blank=True, )
    table_ca4 = models.BooleanField(default=False, blank=True, )

    table_us = models.BooleanField(default=False, blank=True, )

    table_ai1 = models.BooleanField(default=False, blank=True, )
    table_ai2 = models.BooleanField(default=False, blank=True, )
    table_ai3 = models.BooleanField(default=False, blank=True, )
    table_ai4 = models.BooleanField(default=False, blank=True, )

    table_rad1 = models.BooleanField(default=False, blank=True, )
    table_rad2 = models.BooleanField(default=False, blank=True, )
    table_rad3 = models.BooleanField(default=False, blank=True, )
    def __str__(self):
        return f"UI #{self.inst_use_id}"

class AncillaryInstruments(models.Model):
    ai_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )
    
    tacker = models.BooleanField(default=False, blank=True)
    clips = models.BooleanField(default=False, blank=True)
    staplers_l = models.BooleanField(default=False, blank=True)
    staplers_c = models.BooleanField(default=False, blank=True)
    other = models.BooleanField(default=False, blank=True)
    comment = models.TextField(default=" ", blank=True)

    monopolar = models.BooleanField(default=False, blank=True)
    bipolar = models.BooleanField(default=False, blank=True)
    ultrasound = models.BooleanField(default=False, blank=True)
    high_energy_device = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"AI #{self.ai_id}"

class PostProcedural(models.Model):
    postproc_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )

    brought_ICU = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")
    start_ICU = models.DateTimeField(blank=True, null=True, default=timezone.now())
    end_ICU = models.DateTimeField(blank=True, null=True, default=timezone.now())

    generic_name_l1 = models.CharField(max_length=100, blank=True, null=True, default="Нет")
    dose_l1 = models.IntegerField(blank=True, default=0)
    unit_l1 = models.CharField(max_length=10, blank=True, null=True, default="Нет")

    generic_name_l2 = models.CharField(max_length=100, blank=True, null=True, default="Нет")
    dose_l2 = models.IntegerField(blank=True, null=True, default=0)
    unit_l2 = models.CharField(max_length=10, blank=True, null=True, default="Нет")

    generic_name_l3 = models.CharField(max_length=100, blank=True, null=True, default="Нет")
    dose_l3 = models.IntegerField(blank=True, null=True, default=0)
    unit_l3 = models.CharField(max_length=10, blank=True, null=True, default="Нет")

    datetime_discharge = models.DateTimeField(blank=True, null=True, default=timezone.now())
    adverse_event_noted = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")
    def __str__(self):
        return f"PP #{self.postproc_id}"

class FollowUp(models.Model):
    fu_id = models.AutoField(primary_key=True)
    card_id = models.OneToOneField(
        Card,
        on_delete=models.CASCADE,
        default=0
    )

    date_followup = models.DateField(blank=True, null=True, default=timezone.now())
    any_AE = models.CharField(max_length=3, choices=YESNO_CHOICES, default="Нет")
    def __str__(self):
        return f"FU #{self.fu_id}"
