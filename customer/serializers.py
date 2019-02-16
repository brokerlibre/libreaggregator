from rest_framework import serializers
from . import models


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name',)
        model = models.Customer

