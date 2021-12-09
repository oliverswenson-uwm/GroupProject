from django.test import TestCase
from DataLog.models import *


class TestCreateCourse(TestCase):
    def setUp(self):
        self.courseExist = Course(name="CS999", section=123, credits=3, prereqs="None", description="Fun")
        self.courseExist.save()
        self.labExist = Lab(name="CS999", section=321)
        self.labExist.save()
        print(Lab.objects.all())

    def test_none(self):
        lab = Admin.createLab(self, None, None)
        self.assertIsNone(lab, "Cannot create lab with None type fields")

    def test_empty(self):
        lab = Admin.createLab(self, "", "")
        self.assertIsNone(lab, "Cannot create lab with empty fields")

    def test_whiteSpace(self):
        lab = Admin.createLab(self, " ", " ")
        self.assertIsNone(lab, "Cannot create lab with empty fields")

    def test_intTypeName(self):
        lab = Admin.createLab(self, 123, 801)
        self.assertIsNone(lab, "Cannot create lab with int type name fields")

    def test_badName(self):
        lab = Admin.createLab(self, "-CS361", 801)
        self.assertIsNone(lab, "Cannot create lab with special char in front of name fields")

    def test_negSec(self):
        lab = Admin.createLab(self, "CS361", -801)
        self.assertIsNone(lab, "Cannot create lab with negative section fields")

    def test_zeroSec(self):
        lab = Admin.createLab(self, "CS361", 0)
        self.assertIsNone(lab, "Cannot create lab with section 0 fields")

    def test_badSec(self):
        lab = Admin.createLab(self, "CS361", 9999999)
        self.assertIsNone(lab, "Cannot create lab with big section fields")

    def test_labExist(self):
        lab = Admin.createLab(self, "CS999", 321)
        self.assertIsNone(lab, "Cannot create lab since new lab already exist")

    def test_labSimilarToCourse(self):
        lab = Admin.createLab(self, "CS999", 123)
        print(lab)
        self.assertIsNone(lab, "Cannot create lab similar to course")

    def test_courseNotExit(self):
        lab = Admin.createLab(self, "CS111", 321)
        self.assertIsNone(lab, "Cannot create lab without course being in existence")

    def test_newLab(self):
        lab = Admin.createLab(self, "CS999", 456)
        self.assertEquals("CS999-456", lab.__str__(), "Lab was not created")
