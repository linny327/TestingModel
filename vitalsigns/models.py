from django.db import models


# Create your models here.
class VitalSigns(models.Model):
    vitals = models.CharField(max_length=100)
    vitals1 = models.CharField(max_length=100)
    vitals2 = models.CharField(max_length=100)

    def __str__(self):
        return self.vitals, self.vitals1, self.vitals2

