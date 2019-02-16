from rest_framework import serializers
from . import models


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'totalvalue', 'share', 'broker', 'Customer',
                 'paymentdate', 'startdate', 'enddate')
        model = models.Sale

