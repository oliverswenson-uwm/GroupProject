from django.test import TestCase
from DataLog.models import *


class test_Ta_Lab(TestCase):

    def test_add_Ta_Lab_One(self):
        ta1 = Admin.createTA(self, fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        Admin.createCourse(self, nm="Math101", sec="401", cre="3", pre="none", des="None")
        lab1 = Admin.createLab(self, name="Math101", section=801)
        temp = Professor.assignTA(self, "testTAone", "Math101", 801)
        self.assertEqual(temp.ta.name, ta1.name)
        self.assertEqual(temp.lab.name, lab1.name)
        self.assertEqual(temp.lab.section, lab1.section)

    def test_No_TA(self):
        Admin.createCourse(self, nm="COMPSCI361", sec="401", cre="3", pre="none", des="None")
        lab2 = Lab(self, name="COMPSCI361", section=801)
        # temp = Professor.add_taLab(self, None, lab2)
        temp = Professor.assignTA(self, None, lab2.name, lab2.section)
        self.assertEqual(temp, None)

        tem = Professor.assignTA(self, "", lab2.name, lab2.section)
        self.assertEqual(tem, None)

    def test_no_Lab(self):
        ta3 = Admin.createTA(self, fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        temp = Professor.assignTA(self, ta3, None, None)

        self.assertEqual(temp, None)

        tem = Professor.assignTA(self, ta3, "", "")
        self.assertEqual(tem, None)

    def test_Invalid_TA_Noname(self):
        ta4 = Admin.createTA(self, fullName="", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        Admin.createCourse(self, nm="COMPSCI337", sec="401", cre="3", pre="none", des="None")
        lab4 = Admin.createLab(self, name="COMPSCI337", section=901)
        self.assertEqual(Professor.assignTA(self, ta4, lab4.name, lab4.section), None)

    def test_Invalid_TA_Noemail(self):
        ta5 = Admin.createTA(self, fullName="", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab5 = Lab(self, name="COMPSCI337", section=901)
        self.assertEqual(Professor.assignTA(self, ta5, lab5.name, lab5.section), None)

    def test_Invalid_Lab_NoName(self):
        ta6 = Admin.createTA(self, fullName="ta1", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab6 = Admin.createLab(self, name="", section=802)
        self.assertEqual(Professor.assignTA(self, ta6.username, lab6, lab6), None)

    def test_Invalid_Lab_NoSection(self):
        ta7 = Admin.createTA(self, fullName="ta1", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab7 = Admin.createLab(self, name="compsci361", section="")
        self.assertEqual(Professor.assignTA(self, ta7.username, lab7, lab7), None)

    def test_Invalid_Lab_InvalidSection(self):
        ta8 = Admin.createTA(self, fullName="ta1", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab8 = Admin.createLab(self, name="compsci361", section="asdf")
        self.assertEqual(Professor.assignTA(self, ta8.username, lab8, lab8), None)

    def test_Invalid_Lab_InvalidName(self):
        ta9 = Admin.createTA(self, fullName="ta1", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab9 = Admin.createLab(self, name="@compsci361", section=801)
        self.assertEqual(Professor.assignTA(self, ta9.username, lab9, lab9), None)

    def test_ValidLab_NoCourse(self):
        ta10 = Admin.createTA(self, fullName="ta1", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab10 = Admin.createLab(self, name="PHYSICS101", section=901)
        self.assertEqual(Professor.assignTA(self, ta10.username, lab10, lab10), None)