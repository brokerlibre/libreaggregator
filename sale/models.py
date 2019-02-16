from django.db import models
from broker.models import Broker
from customer.models import Customer

import datetime

class Sale(models.Model):
    name = models.CharField(default='sale', max_length=100)
    totalvalue = models.FloatField(default=0.0)
    share = models.FloatField(default=0.0)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE, default=None)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    paymentdate = models.DateField(default=datetime.date.today)
    startdate = models.DateField(default=datetime.date.today)
    enddate= models.DateField(default=datetime.date.today)
        

    def __str__(self):
        return self.name
