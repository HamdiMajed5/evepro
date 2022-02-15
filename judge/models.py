from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Judge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=60)
    category = models.ForeignKey('category.category',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.category.name}'