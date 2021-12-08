from django.test import TestCase
from DataLog.models import Staff, TA, Professor, Admin

class TestCreateAdminGood(TestCase):

    def testAdminGoodOne(self):
        Admin.createAdmin(self, fullName = "TestAdminone", email = "adminonetest@gmail.com", username = "adminonetestuser",
                          password = "adminpassone", phNumber = 9529529952, mailAdrs = "123 AdminTest Way")
        temp = Staff.getUser(self, "adminonetestuser")
        self.assertEqual(temp.username,"adminonetestuser")

    def testAdminGoodTwo(self):
        Admin.createAdmin(self, fullName="TestAdminTwo", email="admintwotest@gmail.com", username="admintwotestUser",
                          password="adminpasstwo", phNumber=1234512311, mailAdrs="234 AdminTest Blvd")
        temp = Staff.getUser(self, "admintwotestUser")
        self.assertEqual(temp.username, "admintwotestUser")


class TestCreateProfGood(TestCase):


    def testProfGoodOne(self):
        Admin.createProf(self, fullName="TestprofOne", email="proftesting1@gmail.com", username="testprofoneuser",
                          password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        temp = Staff.getUser(self, "testprofoneuser")
        self.assertEqual(temp.username, "testprofoneuser")


    def testProfGoodTwo(self):
        Admin.createProf(self, fullName="TestprofTwo", email="proftesting2@gmail.com", username="testproftwouser",
                          password="profpasstwo", phNumber=2222222221, mailAdrs="2 Education Circle")
        temp = Staff.getUser(self, "testproftwouser")
        self.assertEqual(temp.username, "testproftwouser")


class TestCreateTaGood(TestCase):

    def testTaGoodTwo(self):
        Admin.createTA(self, fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                          password="testpassoneTA", phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        temp = Staff.getUser(self, "testTAone")
        self.assertEqual(temp.username, "testTaone")


    #numerical username
    def testTaGoodTwo(self):
        Admin.createTA(self, fullName="TestTAtwo", email="tatester222@gmail.com", username="TA2user",
                          password="testTA2PASS", phNumber=9999999999, mailAdrs="3 TeachingAssistant Lane")
        temp = Staff.getUser(self, "TA2user")
        self.assertEqual(temp.username, "TA2user")



class TestInvalidInputDontAccept(TestCase):

    def testInvalidPhoneProf(self):

        Admin.createProf(self, fullName="invalidPhoneProf", email="phonebad@gmail.com", username="newphoneplz",
                         password="nophone", phNumber="abcdefg", mailAdrs="7 payphone Lane")
        temp = Staff.getUser(self, "newphoneplz")
        self.assertEqual(temp, None)#shouldnt create account because phonenumber is invalid

    def testInvalidPhoneTA(self):

        Admin.createTA(self, fullName="invalidPhoneTA", email="badphone@gmail.com", username="invalidTA",
                       password="nophone2", phNumber="", mailAdrs="3 Telephone Way")
        temp = Staff.getUser(self, "invalidTA")
        self.assertEqual(temp, None)  # shouldnt create account because phonenumber is not int

    def testInvalidPhoneAdmin(self):

        Admin.createAdmin(self, fullName="invalidPhoneAdmin", email="Adminbadphone@gmail.com", username="adminhelpme",
                          password="nophoneadmin", phNumber=12345678889, mailAdrs="7 admin Lane")
        temp = Staff.getUser(self, "adminhelpme")
        self.assertEqual(temp, None)  # shouldnt create account because phonenumber is one digit too large

    def testInvalidEmail(self):
        pass

    def testBlankFields(self):
        Admin.createAdmin(self, fullName="", email="", username="pleasedontcreate",
                          password="", phNumber=1234567888, mailAdrs="")
        temp = Staff.getUser(self, "pleasedontcreate")
        self.assertEqual(temp, None)  # shouldnt create account because phonenumber is one digit too large

        Admin.createProf(self, fullName="", email="", username="dontcreatethisProf",
                          password="", phNumber=0, mailAdrs="")
        temp = Staff.getUser(self, "dontcreatethisProf")
        self.assertEqual(temp, None)  # shouldnt create account because phonenumber is one digit too large

        Admin.createTA(self, fullName="", email="", username="dontcreatethisTA",
                          password="", phNumber=0, mailAdrs="")
        temp = Staff.getUser(self, "dontcreatethisTA")
        self.assertEqual(temp, None)  # shouldnt create account because phonenumber is one digit too large

class TestGetNonexistant(TestCase):

    #test to make sure the function doesn't just return the argument, should return none if nonexistant
    def testGetNonexistant(self):
        temp = Staff.getUser(self, "nonexistantUser")
        self.assertNotEqual(temp, "nonexistantUser")
        self.assertEqual(temp, None)