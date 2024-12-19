from rest_framework import serializers
from .models import Driver, DriverRequest, Reklama


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class DriverRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverRequest
        fields = '__all__'


class ReklamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reklama
        fields = '__all__'