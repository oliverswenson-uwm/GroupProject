from django.test import TestCase
# from myapp.models import (USER) test
from django.test import Client
from GroupNullProject.models import *

class AssignUser():

    def SetUp(self):
        self.client = Client()
        user = User(name="role", password="password")
        user.save()

    def test_validUser(self):
        pass

    def test_invalidUser(self):
        pass

    def test_validCourse(self):
        pass

    def test_inValidCourse(self):
        pass

    def test_assignTAToLab(self):
        pass

    def test_assignTAToCourse(self):
        pass

    def test_assignInstructorToLab(self):
        pass

    def test_assignInstructorToCourse(self):
        pass

    def test_assignDuplicateToCourse(self):
        pass

    def test_assignMultipleSections(self):
        pass

    def test_assignMultipleInsturctors(self):
        pass
