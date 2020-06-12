from django.db import models
from accounts.models import Patient,Doctor
class Appointment(models.Model):
    aid=models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,default="Pending")
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    def __str__(self):
        return str(self.aid)