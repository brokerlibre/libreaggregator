from rest_framework import serializers
from . import models


class InsurerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name',)
        model = models.Insurer

