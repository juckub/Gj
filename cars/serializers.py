from rest_framework import serializers
from demorest.cars.models import Car


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
