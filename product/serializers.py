from rest_framework import serializers
from .models import Product, Service

class ProductSerializer(
    serializers.ModelSerializer
):
    class Meta: 
        model = Product
        fields = (
            "title",
            "subtitle",
            "uploaded_at",
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
            "uploaded_at",
            "parent_organization"

        )
