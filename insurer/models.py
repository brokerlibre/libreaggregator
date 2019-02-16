from django.db import models


class Insurer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
