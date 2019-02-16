from django.db import models

class Customer(models.Model):
    name = models.CharField(default='name', max_length=100)
    cellphone = models.CharField(default='(00) 99999-9999', max_length=100)
    email = models.CharField(default='name@email.com', max_length=100)
    cpf = models.CharField(default='000.000.000-00', max_length=100)
    telegram = models.CharField(default='@name', max_length=100)
    facebook = models.CharField(default='name', max_length=100)
    income= models.FloatField(default=0.0)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
