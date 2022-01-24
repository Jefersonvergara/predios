from django.db import models



# Create your models here.


    
class Owner(models.Model):
    name = models.CharField(max_length=100)
    date_created= models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Properties(models.Model):
    propietario = models.ForeignKey(Owner, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    latitud = models.CharField(max_length=100, null=True)
    longitud = models.CharField(max_length=100, null=True)
    date_created= models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name_propietario
    
    