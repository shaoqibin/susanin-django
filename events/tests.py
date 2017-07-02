from django.test import TestCase

from .models import Guide
from events.models import Event
# Create your tests here.



class GuideModelTests(TestCase):

    def setUp(self):
        pass

    def test_check_guide(self):
        a = Guide(name='joe')
        self.assertIs(a.name,'joe')

    def test_init_url_flat(self):
        events_list=Event.objects.values_list('permalink',flat=True)
        events_list=list(events_list)
        events_list='|'.join(events_list)
        self.assertIs(events_list, '')

