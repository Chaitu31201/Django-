from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length = 20,unique = True )
    age = models.IntegerField()
    phno = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.uname)
class Guest(models.Model):
    name = models.CharField(max_length = 20,unique = True)
    age = models.IntegerField(max_length = 10)
    vehicle_no = models.CharField(max_length = 10)
    def __str__(self):
        return str(self.name)
