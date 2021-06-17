from rest_framework import serializers
from .models import Product, Service, PriceObj

class ProductSerializer(
    serializers.ModelSerializer
):
    class Meta: 
        model = Product
        fields = (
            "title",
            "subtitle",
            "created_at",
            "parent_organization"
        )
class ServiceSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Service
        fields = (
            "title",
            "is_recurring",
            "created_at",
            "parent_organization"

        )

class ProductPriceObjSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = PriceObj
        fields = (
            "title",
            "amount",
            "parent_product",
            "is_recurring",
            "recurrence_freq"
        )
