from django.test import TestCase
from DataLog.models import *


class test_Ta_Lab(TestCase):
    def setUp(self):
        self.admin = Admin(name="TestAdminone", email="adminonetest@gmail.com", username="adminonetestuser",
                           password="adminpassone", phoneNum=9529529952, mailAddress="123 AdminTest Way")
        self.prof1 = self.admin.createProf(fullName="TestprofOne", email="proftesting1@gmail.com",
                                           username="testprofoneuser",
                                           password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        self.ta1 = self.admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                                       password="testpassoneTA",
                                       phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        self.course1 = self.admin.createCourse(nm="MATH240", sec="001", cre="3", pre="None", des="matrices")
        self.lab1 = self.admin.createLab(name="MATH240", labSection=801, courseSection=1)
        self.lab2 = self.admin.createLab(name="compsci314", labSection=802, courseSection=1)

    def test_add_Ta_Lab_One(self):
        temp = self.prof1.assignTA(self.ta1.username, self.lab1.name, self.lab1.section)
        self.assertEqual(temp.ta.name, self.ta1.name)
        self.assertEqual(temp.lab.name, self.lab1.name)
        self.assertEqual(temp.lab.section, self.lab1.section)

    def test_No_TA(self):
        temp = self.prof1.assignTA(None, self.lab1.name, self.lab1.section)
        self.assertEqual(temp, None)

        tem = self.prof1.assignTA("", self.lab1.name, self.lab1.section)
        self.assertEqual(tem, None)

    def test_no_Lab(self):
        temp = self.prof1.assignTA(self.ta1.username, None, None)

        self.assertEqual(temp, None)

        tem = self.prof1.assignTA(self.ta1.username, "", "")
        self.assertEqual(tem, None)

    def test_ValidLab_NoCourse(self):
        temp = self.prof1.assignTA(self.ta1.username, self.lab2, self.lab2)
        self.assertEqual(temp, None)
