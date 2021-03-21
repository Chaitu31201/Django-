from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 20,unique = True)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 200)
    def __str__(self):
        return str(self.first_name+" "+self.last_name)
