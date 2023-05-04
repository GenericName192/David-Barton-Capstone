from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=30)
    task = models.CharField(max_length=30, default="Database")

    def __str__(self):
        return self.name