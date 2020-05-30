from django.db import models

import uuid
from django.urls import reverse 



class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this patient')
    Name = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Adresse = models.CharField(max_length=200)
    Phone = models.IntegerField
    
    Doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)
    Records = models.ForeignKey('Records', on_delete=models.SET_NULL, null=True)
  

    
    def __str__(self):
        """String for representing the Model object."""
        return self.Name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this patient."""
        return reverse('patient-detail', args=[str(self.id)])



class Doctor(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    Name = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Field = models.CharField(max_length=200, help_text='field of work for the Doctor')
    Patient = models.ForeignKey('Patient', on_delete=models.SET_NULL, null=True)
    Records = models.ForeignKey('Records', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.Name
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this Doctor."""
        return reverse('Doctor-detail', args=[str(self.id)])


class Records(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    History = models.CharField(max_length=1000)
   
    Doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)
    Patient = models.ForeignKey('Patient', on_delete=models.SET_NULL, null=True)
    