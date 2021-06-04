from rest_framework import serializers
from .models import CareerContact, CareerRole, Company
class CompanySerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Company
        fields = (
            'title',
            "page_url",
            "linked_in_url",
            "company_type",
            "company_size",
            "employee_count"
        )
class CareerContactSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model  = CareerContact
        fields = (
            "first_name",
            "alias",
            "last_name",
            "phone_number",
            "uploaded_at",
            "email",
            "gender",
            "parent_company"
        )

class CareerRoleSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = CareerRole
        fields = (
            "title",
            "parent_company"
        )
