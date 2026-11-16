from django.db import models
from AccountApp.models import Doctor,Patient
# Create your models here.


class Appointement(models.Model):
    reason= models.TextField()
    prescription=models.FileField(
        blank=True,
        upload_to='prescriptions/'
    )
    class Status(models.TextChoices):
        PENDING = "PENDING","En attente"
        CONFIRMED=  "CONFIRMED" ,"Confirmé"
        CANCELLED = "CANCELLED" ,"Annulé"
    status= models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING)

    """status= models.CharField(max_length=10,choices=
        [(Status.PENDING,"En attente"),("CONFIRMED","Confirmé")]
        ,default="PENDING")"""
    duration_minutes=models.IntegerField(default=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    appointment_date=models.DateTimeField()
    
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="appointments")
    patient=models.ForeignKey("AccountApp.Patient",on_delete=models.CASCADE,related_name="appointments")

    def __str__(self):
        return f"Rendez-vous du {self.appointment_date}"

    class Meta:
        ordering=["appointment_date"]
        constraints=[
            models.UniqueConstraint(
                fields=["doctor",'appointment_date'],
                name="unicite_patient_doctor_date",
                violation_error_message="ce docteur possede un rdv avec cette date"
            ),
        ]