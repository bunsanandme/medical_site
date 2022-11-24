from django.contrib import admin
from .models import FollowUp, Pacient, PreprocedureCard, MedicalHistory, Card, SurgicalHistory, GastrointestinalProcedure, UrologicalProcedure, SurgicalProceduralDetail, RoboticArmLocation,TrocardLocation, BloodLoss, RobotMalfunction, InstrumentUsed, AncillaryInstruments, PostProcedural

admin.site.register(Pacient)
admin.site.register(PreprocedureCard)
admin.site.register(MedicalHistory)
admin.site.register(Card)
admin.site.register(SurgicalHistory)
admin.site.register(GastrointestinalProcedure)
admin.site.register(UrologicalProcedure)
admin.site.register(SurgicalProceduralDetail)
admin.site.register(RoboticArmLocation)
admin.site.register(TrocardLocation)
admin.site.register(BloodLoss)
admin.site.register(RobotMalfunction)
admin.site.register(InstrumentUsed)
admin.site.register(AncillaryInstruments)
admin.site.register(PostProcedural)
admin.site.register(FollowUp)