from django.db import models
from django.utils import timezone
from accounts.models import Patient


# Payment Models
class Payment(models.Model):
    pmid=models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    outstanding=models.IntegerField(default=0)
    paid=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.pmid)
