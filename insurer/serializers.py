from rest_framework import serializers
from . import models


class InsurerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'site', 'api')
        model = models.Insurer

