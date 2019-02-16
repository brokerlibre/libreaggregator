from django.db import models


class Insurer(models.Model):
    name = models.CharField(default='insurer', max_length=100)
    site = models.CharField(default='insurer.site.com', max_length=300)
    api = models.CharField(default='api.insurer.site.com', max_length=300)

    def __str__(self):
        return self.name
