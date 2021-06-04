from django.test import TestCase
from .models import Organization, Role, Venture
# Create your tests here.
class GeneralBusinessTestCase(TestCase):
    def setUp(self):
       
        #create mock organization
        self.mock_organization = Organization.objects.create(
            title = "Test Organization",
            subtitle ="Testing this organization.",
            parent_organization = None
        )

        #create mock venture
        self.mock_venture = Venture.objects.create(
            title = "Test Venture",
            subtitle = "Testing this venture.",
            parent_organization = self.mock_organization
        )
        #creates mock role
        self.mock_role = Role.objects.create(
            title = "Test Role",
            subtitle = "Testing this role.",
            parent_organization = self.mock_organization
        )
    def test_organization_is_posted(self):
        """ Organization is created. """
        organization = Organization.objects.get(title = "Test Organization")
        self.assertEqual(organization.subtitle, "Testing this organization.")

    def test_venture_is_posted(self):
        """ Venture is created. """
        venture = Venture.objects.get(
            title = "Test Venture"
        )
        self.assertEqual(venture.subtitle, "Testing this venture.")
    
    def test_role_is_posted(self):
        """ Role is created. """
        role = Role.objects.get(
            title = "Test Role"
        )
        self.assertEqual(role.subtitle, "Testing this role.")