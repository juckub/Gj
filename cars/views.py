from django.shortcuts import render
from rest_framework import generics
from demorest.cars.serializers import CarDetailSerializer


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer