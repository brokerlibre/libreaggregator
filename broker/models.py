from django.db import models


class Broker(models.Model):
    name = models.CharField(default='broker', max_length=100)
    email = models.CharField(default='broker@email.com', max_length=100)
    password = models.CharField(default='password', max_length=100)
    passwordconfirmation = models.CharField(default='passwordconfirmation', max_length=100)

    def __str__(self):
        return self.name
