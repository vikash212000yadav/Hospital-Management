from django.db import models
from django.utils import timezone
from accounts.models import Patient,Doctor


# Prescription Models
class Prescription(models.Model):
    prid=models.AutoField(primary_key=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    prescription=models.TextField()
    disease=models.CharField(max_length=25)
    date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.prid}'
