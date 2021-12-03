from django.test import TestCase
#from myapp.models import (USER)
from django.test import Client


def SetUp(self):
    self.client = Client()
    user = User(name="role", password="password")
    user.save()

class TestCreateValid(TestCase):
    pass

class TestCreateInvalid(TestCase):
    pass

class TestCreateDuplicate(TestCase):
    pass
