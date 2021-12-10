from django.test import TestCase
from DataLog.models import *


class test_Ta_Lab(TestCase):

    def add_Ta_Lab_One(self):
        t = Admin.createTA(self, "TA1", "123@a.com", "TA1", "TA1", "111", "1st")
        l = Admin.createLab(self, "COMPSCI361", "801")
        temp = assignTaToLab(self, t, l)
        self.assertEqual(temp.section, "801")

    def add_Ta_Lab_Two(self):
        t = Admin.createTA(self, "TA2", "123@a.com", "TA2", "TA2", "222", "2nd")
        l = Admin.createLab(self, "COMPSCI361", "801")
        temp = assignTaToLab(self, t, l)
        self.assertEqual(temp.section, "801")

    def no_TA(self):
        l = Admin.createLab(self, "COMPSCI361", "801")
        temp = assignTaToLab(self, None, l)
        self.assertEqual(temp, None)

    def no_Lab(self):
        t = Admin.createTA(self, "TA1", "123@a.com", "TA1", "TA1", "111", "1st")
        temp = assignTaToLab(self, t, None)
        self.assertEqual(temp, None)


