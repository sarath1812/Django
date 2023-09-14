from django.db import models

# Create your models here.

class Department(models.Model) : 
    DepId = models.AutoField(primary_key=True)
    DepName = models.CharField(max_length=100)


