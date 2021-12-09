from django.test import TestCase
from DataLog.models import *


class TestCreateCourse(TestCase):
    def setUp(self):
        self.admin1 = Admin(name="Admin One", email="a1@a.com", username="admin", password="admin", phoneNum="1", mailAddress="WI")
        self.admin1.save()
        self.prof1 = Professor(name="Prof One", email="p1@a.com", username="p1", password="p1", phoneNum="2", mailAddress="NY")
        self.prof1.save()
        self.prof2 = Professor(name="Prof Two", email="p2@a.com", username="p2", password="p2", phoneNum="3", mailAddress="CA")
        self.prof2.save()
        self.ta1 = TA(name="Ta Onw", email="t1@a.com", username="t1", password="t1", phoneNum="4", mailAddress="AA")
        self.ta1.save()
        self.ta2 = TA(name="Ta Two", email="t2@a.com", username="t2", password="t2", phoneNum="5", mailAddress="BB")
        self.ta2.save()
        self.ta3 = TA(name="Ta Three", email="t3@a.com", username="t3", password="t3", phoneNum="6", mailAddress="CC")
        self.ta3.save()
        self.ta4 = TA(name="Ta Four", email="t4@a.com", username="t4", password="t4", phoneNum="7", mailAddress="DD")
        self.ta4.save()

    def test_None(self):
        q = self.admin1.getContactInfo(None)
        self.assertIsNone(q, "None staff type should return nothing")

    def test_empty(self):
        q = self.admin1.getContactInfo("")
        self.assertIsNone(q, "Empty argument should return nothing")

    def test_whiteSpaceArg(self):
        q = self.admin1.getContactInfo(" ")
        self.assertIsNone(q, "Empty argument should return nothing")

    def test_intArg(self):
        q = self.admin1.getContactInfo(3)
        self.assertIsNone(q, "Integer argument should return nothing")

    def test_invalidArg(self):
        q = self.admin1.getContactInfo(["admin"])
        self.assertIsNone(q, "list argument should return nothing")

    def test_adminInfo(self):
        q = self.admin1.getContactInfo("admin")
        x = q[0]
        self.assertEquals(self.admin1.email, x.email, "Contact info is not return correctly")

    def test_profInfo(self):
        q = self.admin1.getContactInfo("prof")
        x1 = q[0]
        x2 = q[1]
        self.assertEquals(self.prof1.email, x1.email, "Contact info is not return correctly")
        self.assertEquals(self.prof2.email, x2.email, "Contact info is not return correctly")

    def test_taInfo(self):
        q = self.admin1.getContactInfo("ta")
        x1 = q[0]
        x2 = q[1]
        x3 = q[2]
        x4 = q[3]
        self.assertEquals(self.ta1.email, x1.email, "Contact info is not return correctly")
        self.assertEquals(self.ta2.email, x2.email, "Contact info is not return correctly")
        self.assertEquals(self.ta3.email, x3.email, "Contact info is not return correctly")
        self.assertEquals(self.ta4.email, x4.email, "Contact info is not return correctly")
