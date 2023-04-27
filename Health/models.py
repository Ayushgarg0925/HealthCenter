from django.db import models

Department=[
    ("General Health","General Health"),
    ("Cardiology","Cardiology"),
    ("Dental","Dental"),
    ("Medical Reasearch","Medical Reasearch"),
]

class Patient(models.Model):
    pname=models.CharField(max_length=100)
    pemail=models.EmailField()
    pdate=models.DateField(max_length=50)
    pdept=models.CharField(max_length=20,default='Select',choices=Department)
    pcontact=models.CharField(max_length=15)
    pmsg=models.CharField(max_length=100)
    class Meta:
        db_table="Patientinfo"
