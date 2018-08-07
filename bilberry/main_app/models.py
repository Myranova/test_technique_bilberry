from django.db import models

# Create your models here.

class Photo(models.Model):
    nom = models.CharField(max_length = 255)
    photo = models.ImageField()
    timestamp = models.CharField(max_length=100) #timestamp maybe a  date
    verified_flag = models.BooleanField()
    rejected_flag = models.BooleanField()
    
    def __str__(self):
        return self.nom

#Image.objects.create(path=".", timestamp=".", verified_flag=0, rejected_flag=0)