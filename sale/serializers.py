from rest_framework import serializers
from . import models


class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name',)
        model = models.Sale

