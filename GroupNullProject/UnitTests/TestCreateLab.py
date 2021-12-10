from django.test import TestCase
from DataLog.models import *


class TestCreateLab(TestCase):
    def setUp(self):
        self.admin = Admin(name="Admin One", email="a1@a.com", username="admin", password="admin", phoneNum="1", mailAddress="WI")
        self.admin.save()
        self.courseExist = Course(name="CS999", section=123, credits=3, prereqs="None", description="Fun")
        self.courseExist.save()
        self.labExist = Lab(name="CS999", section=321)
        self.labExist.save()

    def test_none(self):
        lab = self.admin.createLab(None, None)
        self.assertIsNone(lab, "Cannot create lab with None type fields")

    def test_empty(self):
        lab = self.admin.createLab("", "")
        self.assertIsNone(lab, "Cannot create lab with empty fields")

    def test_whiteSpace(self):
        lab = self.admin.createLab(" ", " ")
        self.assertIsNone(lab, "Cannot create lab with empty fields")

    def test_intTypeName(self):
        lab = self.admin.createLab(123, 801)
        self.assertIsNone(lab, "Cannot create lab with int type name fields")

    def test_badName(self):
        lab = self.admin.createLab("-CS361", 801)
        self.assertIsNone(lab, "Cannot create lab with special char in front of name fields")

    def test_negSec(self):
        lab = self.admin.createLab("CS361", -801)
        self.assertIsNone(lab, "Cannot create lab with negative section fields")

    def test_zeroSec(self):
        lab = self.admin.createLab("CS361", 0)
        self.assertIsNone(lab, "Cannot create lab with section 0 fields")

    def test_badSec(self):
        lab = self.admin.createLab("CS361", 9999999)
        self.assertIsNone(lab, "Cannot create lab with big section fields")

    def test_labExist(self):
        lab = self.admin.createLab("CS999", 321)
        self.assertIsNone(lab, "Cannot create lab since new lab already exist")

    def test_labSimilarToCourse(self):
        lab = self.admin.createLab("CS999", 123)
        print(lab)
        self.assertIsNone(lab, "Cannot create lab similar to course")

    def test_courseNotExit(self):
        lab = self.admin.createLab("CS111", 321)
        self.assertIsNone(lab, "Cannot create lab without course being in existence")

    def test_newLab(self):
        lab = self.admin.createLab("CS999", 456)
        self.assertEquals("CS999-456", lab.__str__(), "Lab was not created")
