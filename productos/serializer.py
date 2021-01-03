from rest_framework import serializers

from .models import Cerveza


class CervezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cerveza
        fields = '__all__'
