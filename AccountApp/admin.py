from AppointmentApp.models import Appointement
from AccountApp.models import User, Patient, Doctor, Speciality
from django.contrib import admin

# Register your models here.
admin.site.register(User)
admin.site.register(Patient)

class AppointementStacked(admin.StackedInline):
    model = Appointement
    extra = 1

class DoctorPersoClass(admin.ModelAdmin):
    inlines = [AppointementStacked]

admin.site.register(Doctor,DoctorPersoClass)
admin.site.register(Speciality)