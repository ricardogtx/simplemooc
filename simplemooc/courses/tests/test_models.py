from django.test import TestCase
from django.core import mail
from django.test.client import Client
from django.urls import reverse
from django.conf import settings

from model_mommy import mommy

from simplemooc.courses.models import Course

class CourseManagerTestCase(TestCase):
    def setUp(self):
        self.courses_django = mommy.make(
            'courses.Course', name='Python na Web com Django',_quantity=10
        )
        self.courses_dev = mommy.make(
            'courses.Course', name='Python na Web com Devs',_quantity=10
        )
        self.client = Client()
    
    def tearDown(self):
        Course.objects.all().delete()
    
    def test_course_search(self):
        search = Course.objects.filter(name__contains='Django')
        self.assertEqual(len(search),10)
        search = Course.objects.filter(name__contains='devs')
        self.assertEqual(len(search),10)
