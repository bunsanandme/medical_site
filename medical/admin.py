from django.contrib import admin
from .models import Pacient, PreprocedureCard, MedicalHistory, Card

admin.site.register(Pacient)
admin.site.register(PreprocedureCard)
admin.site.register(MedicalHistory)
admin.site.register(Card)
