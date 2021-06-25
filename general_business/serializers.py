from rest_framework import serializers
from .models import Organization, Role, Venture
class OrganizationSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Organization
        fields = (
            'title',
            "subtitle",
            "parent_organization",
            "is_owned_by_me"
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


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            "title",
            "subtitle",
            "parent_organization"
        )

