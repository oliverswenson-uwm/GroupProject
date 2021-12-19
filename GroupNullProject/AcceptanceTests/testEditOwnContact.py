from django.test import TestCase
from DataLog.models import Staff, Admin, Professor, TA
from django.test import Client


class TestEditValid(TestCase):

    def setUp(self):
        client = None
        client = Client()

    def testEditAdmin(self):
        Admin.createProf(self, fullName="ArchiveAdmin", email="Archivethisadmin@gmail.com", username="adminarchive",
                          password="adminarchiveme", phNumber=1234567889, mailAdrs="7 admin Lane")

        resp = self.client.post("/editownacc/", {"phNum": "1112222111", "username": "adminarchive", "mailAdrs" : "123 Changed Lane"
                                                 }, follow=True)
        self.assertEqual("Success! Account info updated.", resp.context["msg"], "Account didn't edit but it shouldve")


    def testEditTA(self):
        Admin.createAdmin(self, fullName="ArchiveAdminTwo", email="Archivethisadminagain@gmail.com", username="archivemetoo",
                          password="archivepass", phNumber=1112221211, mailAdrs="7 archive Lane")

        resp = self.client.post("/archiveacc/", {"email": "Archivethisadminagain@gmail.com", "username": "archivemetoo", "password": "archivepass",
                                                 "accType": "Admin"
                                                 }, follow=True)
        self.assertEqual("Success! Archived account.", resp.context["msg"], "Account didn't archive but it shouldve")

    #if only enter username of account should still find and archive the account
    #(for ease for admin if they forget street address or phone number)
    def testEditProf(self):
        Admin.createAdmin(self, fullName="ArchiveAdminTwo", email="Archivethisadminagain@gmail.com",
                          username="archivemetoo",
                          password="archivepass", phNumber=1112221211, mailAdrs="7 archive Lane")

        resp = self.client.post("/archiveacc/", {"email": "", "username": "archivemetoo",
                                                 "password": "",
                                                 "accType": "Admin"
                                                 }, follow=True)

        self.assertEqual("Success! Archived account.", resp.context["msg"], "Account didn't archive but it shouldve")


#INVALID TESTS
class TestArchiveInvalid(TestCase):

    def setUp(self):
        client = None
        client = Client()

    def testMissingFields(self):
        Admin.createAdmin(self, fullName="ArchiveAdminTwo", email="Archivethisadminagain@gmail.com",
                          username="archivemetoo",
                          password="archivepass", phNumber=1112221211, mailAdrs="7 archive Lane")

        resp = self.client.post("/archiveacc/", {"email": "", "username": "",
                                                 "password": "",
                                                 "accType": ""
                                                 }, follow=True)

        self.assertEqual("Failed to archive account. Double check the information entered", resp.context["msg"], "Recieved success message when should have recieved error")

    def testArchiveTwice(self):
        Admin.createAdmin(self, fullName="ArchiveAdmin", email="Archivethisadmin@gmail.com", username="adminarchive",
                          password="adminarchiveme", phNumber=1234567889, mailAdrs="7 admin Lane")

        self.client.post("/archiveacc/", {"email": "Archivethisadmin@gmail.com", "username": "adminarchive",
                                                 "password": "adminarchiveme",
                                                 "accType": "Admin"
                                                 }, follow=True)
        resp = self.client.post("/archiveacc/", {"email": "Archivethisadmin@gmail.com", "username": "adminarchive",
                                                 "password": "adminarchiveme",
                                                 "accType": "Admin"
                                                 }, follow=True)

        self.assertEqual("Failed to archive account. Double check the information entered", resp.context["msg"], "Account archived twice")
