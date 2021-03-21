from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 20)
    name = models.CharField(max_length = 30)
    pwd = models.CharField(max_length = 20)
    vpwd = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 200,unique = True)
    def __str__(self):
        return str(self.name+" @"+self.username)
