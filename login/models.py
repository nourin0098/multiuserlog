from django.db import models

# Create your models here.
class TbLogin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    USER_TYPES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('pharmacist', 'Pharmacist'),
    )
    type = models.CharField(max_length=20, choices=USER_TYPES)