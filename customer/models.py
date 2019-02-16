from django.db import models

import datetime

class Customer(models.Model):
    name = models.CharField(default='customer', max_length=100)
    cellphone = models.CharField(default='(00) 99999-9999', max_length=100)
    email = models.CharField(default='name@email.com', max_length=100)
    cpf = models.CharField(default='000.000.000-00', max_length=100)
    telegram = models.CharField(default='@name', max_length=100)
    facebook = models.CharField(default='name', max_length=100)
    income= models.FloatField(default=0.0)
    signupdate= models.DateField(default=datetime.date.today)
    birthdate= models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
