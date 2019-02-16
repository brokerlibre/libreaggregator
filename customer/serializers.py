from rest_framework import serializers
from . import models


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'cellphone', 'email', 'cpf', 'telegram', 'facebook',
                 'income', 'signupdate', 'birthdate')
        model = models.Customer

