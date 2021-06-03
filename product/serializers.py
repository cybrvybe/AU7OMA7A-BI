from rest_framework import serializers
from .models import Product, Service, Feature

class ProductSerializer(
    serializers.ModelSerializer
):
    class Meta: 
        model = Product
        fields = (
            "title",
            "subtitle",
            "parent_organization"
        )
class ServiceSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Service
        fields = (
            "title",
            "subtitle",
            "parent_organization"
        )
class FeatureSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Feature
        fields = (
            "title",
            "subtitle", 
            "parent_organization"
        )