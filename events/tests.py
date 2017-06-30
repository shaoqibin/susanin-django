from django.test import TestCase

from .models import Guide
# Create your tests here.



class GuideModelTests(TestCase):

    def test_check_guide(self):
        a = Guide(name='joe')
        self.assertIs(a.name,'joe')
