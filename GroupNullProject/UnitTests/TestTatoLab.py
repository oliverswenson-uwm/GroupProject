from django.test import TestCase
from DataLog.models import *


class test_Ta_Lab(TestCase):

    def test_add_Ta_Lab_One(self):
        ta1 = Admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        Admin.createCourse(nm="Math101", sec="401", cre="3", pre="none", des="None")
        lab1 = Admin.createLab(name="Math101", section=801)
        temp = Admin.add_taLab(ta1, lab1)
        self.assertEqual(temp.ta.name, "TestTAone")
        self.assertEqual(temp.lab.name, "Math101")
        self.assertEqual(temp.lab.section, 801)
        self.assertEqual(temp.lab.name, temp.getLab().name)
        self.assertEqual(temp.ta.name, temp.getTa().name)

    def test_No_TA(self):
        Admin.createCourse(nm="COMPSCI361", sec="401", cre="3", pre="none", des="None")
        lab2 = Lab(self, name="COMPSCI361", section=801)
        temp = Admin.add_taLab(None, lab2)
        self.assertEqual(temp, None)

    def test_no_Lab(self):
        ta3 = Admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        temp = Admin.add_taLab(ta3, None)

        self.assertEqual(temp, None)

    def test_Invalid_TA_Noname(self):
        ta4 = Admin.createTA(fullName="", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        Admin.createCourse(nm="COMPSCI337", sec="401", cre="3", pre="none", des="None")
        lab4 = Admin.createLab(name="COMPSCI337", section=901)
        self.assertEqual(Admin.add_taLab(ta=ta4, lab=lab4), None)

    def test_Invalid_TA_Noemail(self):
        ta5 = Admin.createTA(fullName="", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab5 = Lab(self, name="COMPSCI337", section=901)
        self.assertEqual(Admin.add_taLab(ta=ta5, lab=lab5), None)

    def test_Invalid_Lab_NoName(self):
        ta6 = Admin.createTA(fullName="ta1", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab6 = Admin.createLab(name="", section=802)
        self.assertEqual(Admin.add_taLab(ta=ta6, lab=lab6), None)

    def test_Invalid_Lab_NoSection(self):
        ta6 = Admin.createTA(fullName="ta1", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab6 = Admin.createLab(name="compsci361", section="")
        self.assertEqual(Admin.add_taLab(ta=ta6, lab=lab6), None)

    def test_Invalid_Lab_InvalidSection(self):
        ta7 = Admin.createTA(fullName="ta1", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab7 = Admin.createLab(name="compsci361", section="asdf")
        self.assertEqual(Admin.add_taLab(ta=ta7, lab=lab7), None)

    def test_Invalid_Lab_InvalidName(self):
        ta8 = Admin.createTA(fullName="ta1", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab8 = Admin.createLab(name="@compsci361", section=801)
        self.assertEqual(Admin.add_taLab(ta=ta8, lab=lab8), None)

    def test_ValidLab_NoCourse(self):
        ta9 = Admin.createTA(fullName="ta1", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab9 = Admin.createLab(name="PHYSICS101", section=901)
        self.assertEqual(Admin.add_taLab(ta=ta9, lab=lab9), None)
