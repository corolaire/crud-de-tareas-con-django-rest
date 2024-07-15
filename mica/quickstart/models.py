from django.db import models^
from django.core.validators import MinLengthValidator,MaxLengthValidator
import secrets
class user(models.Model):
    username=models.CharField(max_length=50,null=False)
    lastname=models.CharField(MinLengthValidator=4 , MaxLengthValidator=15,null=False)
    age=models.IntegerField(gt=18 ,lt=99)

# Create your models here.
