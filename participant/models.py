from django.db import models

# Create your models here.

class Participant(models.Model):
    qrid=models.IntegerField(unique=True)
    name=models.CharField(max_length=60)
    age=models.IntegerField(null=True,blank=True)
    phone=models.CharField(max_length=60)

    def __str__(self):
        return self.name



