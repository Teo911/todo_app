from django.db import models

# Create your models here.



class todoModel(models.Model):
    content = models.TextField()