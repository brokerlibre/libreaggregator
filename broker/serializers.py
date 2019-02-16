from rest_framework import serializers
from . import models


class BrokerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'email', 'password', 'passwordconfirmation')
        model = models.Broker

