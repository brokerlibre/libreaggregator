from django.db import models

class Sale(models.Model):
    name = models.CharField(default='sale', max_length=100)
    totalvalue = models.FloatField(default=0.0)
    share = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
