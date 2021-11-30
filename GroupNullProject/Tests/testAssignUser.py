from django.test import TestCase
#from myapp.models import (USER)
from django.test import Client

from GroupNullProject.models import *


def SetUp(self):
    self.client = Client()
    user = User(name="role", password="password")
    user.save()

class TestAssignTA(TestCase):
    pass

class TestAssignProf(TestCase):
    pass

class TestAssignAdmin(TestCase):
    pass