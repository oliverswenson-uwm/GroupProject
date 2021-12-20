from django.test import TestCase
from DataLog.models import Staff, Admin, Professor, TA
from django.test import Client


class TestEditValid(TestCase):

    def setUp(self):
        client = None
        client = Client()

    def testEditAdmin(self):
        Admin.createAdmin(self, fullName="ArchiveAdmin", email="Archivethisadmin@gmail.com", username="adminarchive",
                          password="adminarchiveme", phNumber=1234567889, mailAdrs="7 admin Lane")

        resp = self.client.post("/editownacc/", {"phNumber": "1112222111", "username": "adminarchive", "mailAdrs" : "123 Changed Lane"
                                                 }, follow=True)
        self.assertEqual("Success! Account info updated.", resp.context["msg"], "Account didn't edit but it shouldve")


    def testEditTA(self):
        Admin.createTA(self, fullName="EditTA", email="EditthisTA@gmail.com", username="TAedit",
                         password="editme", phNumber=1234567889, mailAdrs="7 editor Lane")

        resp = self.client.post("/editownacc/",
                                {"phNumber": "6666667777", "username": "TAedit", "mailAdrs": "124 Changed Lane"
                                 }, follow=True)
        self.assertEqual("Success! Account info updated.", resp.context["msg"], "Account didn't edit but it shouldve")

    #if only enter username of account should still find and archive the account
    #(for ease for admin if they forget street address or phone number)
    def testEditProf(self):
        Admin.createProf(self, fullName="Editprof", email="Editthisprof@gmail.com", username="Profedit",
                         password="editprof", phNumber=1111114444, mailAdrs="7 edit St")

        resp = self.client.post("/editownacc/",
                                {"phNumber": "6666667777", "username": "Profedit", "mailAdrs": "124 Changed Lane"
                                 }, follow=True)
        self.assertEqual("Success! Account info updated.", resp.context["msg"], "Account didn't edit but it shouldve")


#INVALID TESTS
class TestArchiveInvalid(TestCase):



    def setUp(self):
        client = None
        client = Client()

    def testBadUser(self):
        Admin.createProf(self, fullName="Editprof", email="Editthisprof@gmail.com", username="Profedit",
                         password="editprof", phNumber=1111114444, mailAdrs="7 edit St")

        resp = self.client.post("/editownacc/",
                                {"phNumber": "6666667777", "username": "doesnotexist", "mailAdrs": "124 Changed Lane"
                                 }, follow=True)
        self.assertEqual("Error editing account. Check current username", resp.context["msg"], "Success message for nonexistant account")


