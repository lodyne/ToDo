from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    notes= models.CharField(max_length=100)
    date_created=models.DateField(default=timezone.now)

    def __str__(self):
        return self.id

