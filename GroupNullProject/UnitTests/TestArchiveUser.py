from django.test import TestCase
from DataLog.models import *


class test_Archieved_user(TestCase):

    def test_Ta(self):
        ta1 = Admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA",
                             phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        temp = Admin.archiveAccount(ta1)
        self.assertEqual(temp.name, "TestTAone")
        self.assertEqual(temp.username, "testTAone")
        self.assertEqual(temp.email, "taOnGmail1@gmail.com")
        self.assertEqual(temp.password, "testpassoneTA")
        self.assertEqual(temp.phoneNum, 3334441111)
        self.assertEqual(temp.mailAddress, "2 TeachingAssistant Circle")

    def test_Prof(self):
        prof1 = Admin.createProf(fullName="PROF1", email="prof1@gmail.com", username="prof1", password="proff1",
                                 phNumber=111222333, mailAdrs="1st prof")
        temp = Admin.archiveAccount(prof1)
        self.assertEqual(temp.name, "PROF1")
        self.assertEqual(temp.username, "prof1")
        self.assertEqual(temp.email, "prof1@gmail.com")
        self.assertEqual(temp.password, "proff1")
        self.assertEqual(temp.phoneNum, 111222333)
        self.assertEqual(temp.mailAddress, "1st prof")

    def test_Admin(self):
        admin1 = Admin.createAdmin(fullName="ADMIN1", email="admin1@gmail.com", username="admin1",
                                   password="admin11", phNumber=12341234, mailAdrs="1st admin")
        temp = Admin.archiveAccount(admin1)
        self.assertEqual(temp.name, "ADMIN1")
        self.assertEqual(temp.username, "admin1")
        self.assertEqual(temp.email, "admin1@gmail.com")
        self.assertEqual(temp.password, "admin11")
        self.assertEqual(temp.phoneNum, 12341234)
        self.assertEqual(temp.mailAddress, "1st admin")

    def test_Invalid_User_Fullname(self):
        prof2 = Admin.createProf(fullName="", email="prof2@gmail.com", username="prof2", password="proff2",
                                 phNumber=12312312, mailAdrs="2nd prof")
        temp = Admin.archiveAccount(prof2)
        self.assertEqual(temp, None)

    def test_Invald_User_Email(self):
        ta2 = Admin.createTA(fullName="TA2", email="", username="ta2", password="taa2", phNumber=1231212,
                             mailAdrs="2nd ta")
        temp = Admin.archiveAccount(ta2)
        self.assertEqual(temp, None)

    def test_No_User(self):
        self.assertEqual(Admin.archiveAccount(None), None)
