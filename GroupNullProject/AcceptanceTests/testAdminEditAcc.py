from django.test import TestCase
from DataLog.models import Staff, Admin, Professor, TA
from django.test import Client

''' fullName = request.POST['fullName']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    phNumber = request.POST['phNumber']
    mailAdrs = request.POST['mailAdrs']'''

class TestAdminEditValid(TestCase):

    def setUp(self):
        client = None
        client = Client()

    def testEditPhone(self):
        Admin.createAdmin(self, fullName="EditAdmin", email="EditthisAdmin@gmail.com", username="admineditme",
                          password="admineditpass", phNumber=1234567889, mailAdrs="7 admin Lane")

        resp = self.client.post("/editacc/", {"fullName": "ArchiveAdmin", "phNumber": "111111111","email": "EditthisAdmin@gmail.com",
                                              "password": "admineditpass", "username": "admineditme", "mailAdrs": "7 admin Lane"
                                                 }, follow=True)
        self.assertEqual("Account information has been updated", resp.context["msg"], "Account phone number should have updated")


    def testEditEmail(self):
        Admin.createAdmin(self, fullName="EditAdmin", email="EditthisAdmin@gmail.com", username="admineditme",
                          password="admineditpass", phNumber=1234567889, mailAdrs="7 admin Lane")

        resp = self.client.post("/editacc/", {"fullName": "ArchiveAdmin", "phNumber": "1234567889","email": "THISISEDITED@gmail.com",
                                              "password": "admineditpass", "username": "admineditme", "mailAdrs": "7 admin Lane"
                                                 }, follow=True)
        self.assertEqual("Account information has been updated", resp.context["msg"], "Account phone number should have updated")


    def testEditMultiple(self):
        Admin.createAdmin(self, fullName="EditAdmin", email="EditthisAdmin@gmail.com", username="admineditme",
                          password="admineditpass", phNumber=1234567889, mailAdrs="7 admin Lane")

        resp = self.client.post("/editacc/", {"fullName": "New Name", "phNumber": "1111111111","email": "THISISEDITED@gmail.com",
                                              "password": "newpassword", "username": "admineditme", "mailAdrs": "New Residence Alley"
                                                 }, follow=True)
        self.assertEqual("Account information has been updated", resp.context["msg"], "Account phone number should have updated")


#INVALID TESTS
class TestArchiveInvalid(TestCase):

    def setUp(self):
        client = None
        client = Client()

    def testBadUser(self):
        Admin.createAdmin(self, fullName="EditAdmin", email="EditthisAdmin@gmail.com", username="admineditme",
                          password="admineditpass", phNumber=1234567889, mailAdrs="7 admin Lane")

        resp = self.client.post("/editacc/",
                                {"fullName": "New Name", "phNumber": "1111111111", "email": "THISISEDITED@gmail.com",
                                 "password": "newpassword", "username": "doesnotexist", "mailAdrs": "New Residence Alley"
                                 }, follow=True)
        self.assertEqual("Account doesn't exist.", resp.context["msg"],
                         "Account should not have been updated")
