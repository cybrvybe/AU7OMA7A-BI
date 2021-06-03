from rest_framework import serializers
from .models import Campaign, Organization, Process, Product, Project, Role, Service, Venture, Feature, AlgoUnit
class OrganizationSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Organization
        fields = (
            'title',
            "subtitle",
            "parent_organization"
        )

class ProcessSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Process
        fields = (
            "title",
            "subtitle",
            "parent_organization"
        )
class VentureSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Venture
        fields = (
            "title",
            "subtitle",
            "parent_organization"
        )
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
class CampaignSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Campaign
        fields = (
            "title",
            "subtitle",
            "parent_organization"
        )
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            "title",
            "subtitle",
            "parent_organization"
        )
class AlgoUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgoUnit
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