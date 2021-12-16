from django.test import TestCase
from DataLog.models import Staff, TA, Professor, Admin

class TestCreateAdminGood(TestCase):

    def testAdminGoodOne(self):
        Admin.createAdmin(fullName ="TestAdminone", email ="adminonetest@gmail.com", username ="adminonetestuser",
                          password = "adminpassone", phNumber = 9529529952, mailAdrs = "123 AdminTest Way")
        temp = Staff.getUser("adminonetestuser")
        self.assertEqual(temp.username,"adminonetestuser")

    def testAdminGoodTwo(self):
        Admin.createAdmin(fullName="TestAdminTwo", email="admintwotest@gmail.com", username="admintwotestUser",
                          password="adminpasstwo", phNumber=1234512311, mailAdrs="234 AdminTest Blvd")
        temp = Staff.getUser("admintwotestUser")
        self.assertEqual(temp.username, "admintwotestUser")


class TestCreateProfGood(TestCase):


    def testProfGoodOne(self):
        Admin.createProf(fullName="TestprofOne", email="proftesting1@gmail.com", username="testprofoneuser",
                         password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        temp = Staff.getUser("testprofoneuser")
        self.assertEqual(temp.username, "testprofoneuser")


    def testProfGoodTwo(self):
        Admin.createProf(fullName="TestprofTwo", email="proftesting2@gmail.com", username="testproftwouser",
                         password="profpasstwo", phNumber=2222222221, mailAdrs="2 Education Circle")
        temp = Staff.getUser("testproftwouser")
        self.assertEqual(temp.username, "testproftwouser")


class TestCreateTaGood(TestCase):

    def testTaGoodTwo(self):
        Admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                       password="testpassoneTA", phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        temp = Staff.getUser("testTAone")
        self.assertEqual(temp.username, "testTaone")


    #numerical username
    def testTaGoodTwo(self):
        Admin.createTA(fullName="TestTAtwo", email="tatester222@gmail.com", username="TA2user",
                       password="testTA2PASS", phNumber=9999999999, mailAdrs="3 TeachingAssistant Lane")
        temp = Staff.getUser("TA2user")
        self.assertEqual(temp.username, "TA2user")



class TestInvalidInputDontAccept(TestCase):

    def testInvalidPhoneProf(self):

        Admin.createProf(fullName="invalidPhoneProf", email="phonebad@gmail.com", username="newphoneplz",
                         password="nophone", phNumber="abcdefg", mailAdrs="7 payphone Lane")
        temp = Staff.getUser("newphoneplz")
        self.assertEqual(temp, None)#shouldnt create account because phonenumber is invalid

    def testInvalidPhoneTA(self):

        Admin.createTA(fullName="invalidPhoneTA", email="badphone@gmail.com", username="invalidTA",
                       password="nophone2", phNumber="", mailAdrs="3 Telephone Way")
        temp = Staff.getUser("invalidTA")
        self.assertEqual(temp, None)  # shouldnt create account because phonenumber is not int

    def testInvalidPhoneAdmin(self):

        Admin.createAdmin(fullName="invalidPhoneAdmin", email="Adminbadphone@gmail.com", username="adminhelpme",
                          password="nophoneadmin", phNumber=12345678889, mailAdrs="7 admin Lane")
        temp = Staff.getUser("adminhelpme")
        self.assertEqual(temp, None)  # shouldnt create account because phonenumber is one digit too large

    def testBlankFields(self):
        Admin.createAdmin(fullName="", email="", username="pleasedontcreate",
                          password="", phNumber=1234567888, mailAdrs="")
        temp = Staff.getUser("pleasedontcreate")
        self.assertEqual(temp, None)

        Admin.createProf(fullName="", email="", username="dontcreatethisProf",
                         password="", phNumber=0, mailAdrs="")
        temp = Staff.getUser("dontcreatethisProf")
        self.assertEqual(temp, None)

        Admin.createTA(fullName="", email="", username="dontcreatethisTA",
                       password="", phNumber=0, mailAdrs="")
        temp = Staff.getUser("dontcreatethisTA")
        self.assertEqual(temp, None)

class TestGetNonexistant(TestCase):

    #test to make sure the function doesn't just return the argument, should return none if nonexistant
    def testGetNonexistant(self):
        temp = Staff.getUser("nonexistantUser")
        self.assertNotEqual(temp, "nonexistantUser")
        self.assertEqual(temp, None)