from django.test import TestCase
from DataLog.models import *


class test_Ta_Lab(TestCase):
    # def setUp(self):
        # self.admin = Admin(name="aasdf", email="adminonetest@gmail.com", username="admin",
        #                    password="admin", phoneNum=9529529952, mailAddress="123 AdminTest Way")
        # self.ta1 = self.admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
        #                                password="testpassoneTA",
        #                                phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        # self.lab1 = self.admin.createLab(name="Math101", section=401)

    def test_add_Ta_Lab_One(self):
        ta1 = Admin.createTA(self, fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                                       password="testpassoneTA",
                                       phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab1 = Admin.createLab(self, name="Math101", section=401)
        temp = Admin.assignTatoLab(self, ta1.username, lab1.section)
        self.assertEqual(temp.ta.name, "TA1")

    # def add_Ta_Lab_Two(self):
    #     t = Admin.createTA(self, "TA2", "123@a.com", "TA2", "TA2", "222", "2nd")
    #     l = Admin.createLab(self, "COMPSCI361", "801")
    #     temp = assignTaToLab(self, t, l)
    #     self.assertEqual(temp.section, "801")
    #
    # def no_TA(self):
    #     l = Admin.createLab(self, "COMPSCI361", "801")
    #     temp = assignTaToLab(self, None, l)
    #     self.assertEqual(temp, None)
    #
    # def no_Lab(self):
    #     t = Admin.createTA(self, "TA1", "123@a.com", "TA1", "TA1", "111", "1st")
    #     temp = assignTaToLab(self, t, None)
    #     self.assertEqual(temp, None)


