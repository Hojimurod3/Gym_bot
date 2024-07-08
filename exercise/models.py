# models.py
from django.db import models


class Training(models.Model):
    weight_category = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    intensity = models.CharField(max_length=50)

    def __str__(self):
        return self.weight_category
