from django.db import models

# Create your models here.
class CandidateRegistration(models.Model):
    first_name=models.CharField(max_length=100,default=True)
    last_name=models.CharField(max_length=100,default=True)
    email=models.EmailField(max_length=50,default=True)
    phone=models.CharField(max_length=50,default=True)
    profile=models.CharField(max_length=50)
    reg_number=models.CharField(max_length=50,blank=True)
    reg_date=models.DateField()
    id_number=models.CharField(max_length=50,default=-1)
    address=models.CharField(max_length=200,blank=True)
    password=models.CharField(max_length=50,default='ajay')
    profile_image=models.ImageField(upload_to="uploaded_image/", default=None,null=True)

    def __str__(self):
        return self.last_name + ' '+self.last_name
