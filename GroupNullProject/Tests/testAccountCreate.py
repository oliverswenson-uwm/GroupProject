from django.test import TestCase
from DataLog.models import Staff, Admin, Professor, TA
from django.test import Client


# TODO: add many more fields for creation

# fullName, email, username, password, phNumber, mailAdrs, accType


class TestCreateValid(TestCase):

    def setUp(self):
        client = None
        client = Client()

    def testGoodCreateAdmin(self):
        resp = self.client.post("/createuser/", {"fullName": "adminone", "email": "admin123@gmail.com",
                                                 "username": "adminuserone", "password": "adminpass",
                                                 "phNumber": "4546768988", "mailAdrs": "123 Admin Ln.",
                                                 "accType": "Admin"
                                                 }, follow=True)
        self.assertEqual( "Success: New Account has been create ",resp.context["msg"],
                         "failed creation. One or more fields invalid")

        resp = self.client.post("/createuser/", {"fullName": "admintwo", "email": "admintest@gmail.com",
                                                 "username": "admintwouser", "password": "adminpasstwo",
                                                 "phNumber": "1112223333", "mailAdrs": "150 Admin Blvd.",
                                                 "accType": "Admin"
                                                 }, follow=True)
        self.assertEqual( "Success: New Account has been create ",resp.context["msg"],
                         "failed creation. One or more fields invalid")

    # Create TA accounts
    def testGoodCreateTA(self):
        resp = self.client.post("/createuser/", {"fullName": "nameone", "email": "test123@gmail.com",
                                                 "username": "userone", "password": "passone",
                                                 "phNumber": "1234567890", "mailAdrs": "123 Applesauce Ln.",
                                                 "accType": "TA"
                                                 }, follow=True)
        self.assertEqual( "Success: New Account has been create ",resp.context["msg"],
                         "failed creation. One or more fields invalid")

        resp = self.client.post("/createuser/", {"fullName": "nametwo", "email": "test345@gmail.com",
                                                 "username": "usertwo", "password": "passtwo",
                                                 "phNumber": "9999999999", "mailAdrs": "150 Kenwood Blvd.",
                                                 "accType": "TA"
                                                 }, follow=True)
        self.assertEqual( "Success: New Account has been create ",resp.context["msg"],
                         "failed creation. One or more fields invalid")

    # Create professor accounts
    def testGoodCreateProf(self):
        resp = self.client.post("/createuser/", {"fullName": "profone", "email": "prof123@gmail.com",
                                                 "username": "profusernameone", "password": "profpass",
                                                 "phNumber": "1334667999", "mailAdrs": "7 Professor Circle",
                                                 "accType": "Professor"
                                                 }, follow=True)
        self.assertEqual( "Success: New Account has been create ",resp.context['msg'],
                         "failed creation. One or more fields invalid")

        resp = self.client.post("/createuser/", {"fullName": "proftwo", "email": "proftwo@gmail.com",
                                                 "username": "proftwo", "password": "proftwopass",
                                                 "phNumber": "2222222222", "mailAdrs": "2 Professor way.",
                                                 "accType": "Professor"
                                                 }, follow=True)
        self.assertEqual( "Success: New Account has been create ",resp.context['msg'],
                         "failed creation. One or more fields invalid")


#INVALID TESTS
class TestCreateInvalid(TestCase):

    def setUp(self):
        client = None
        client = Client()
        Professor(name="ProfessorMan", email="profthree@uwm.edu", username="ProfThree", password="Profpassthree",
                  phoneNum="1234567777", mailAddress="123 Professor ln.").save()

    def testMissingFields(self):
        # all blank
        resp = self.client.post("/createuser/", {"fullName": "", "email": "",
                                                 "username": "", "password": "",
                                                 "phNumber": "", "mailAdrs": "",
                                                 "accType": ""
                                                 }, follow=True)
        self.assertEqual("Failed: A empty field in form", resp.context['msg'],
                         "blank username worked. user: , pass:passone")

    def testBlankFields(self):
        # all blank
        resp = self.client.post("/createuser/", {"fullName": " ", "email": " ",
                                                 "username": " ", "password": " ",
                                                 "phNumber": " ", "mailAdrs": " ",
                                                 "accType": " "
                                                 }, follow=True)
        self.assertEqual("Failed: A empty field in form", resp.context['msg'],
                         "blank username worked. user: , pass:passone")

    def testDuplicateUserName(self):
        #creating user in database to duplicate
        resp = self.client.post("/createuser/", {"fullName": "UniqueName", "email": "uniqueEmail@uwm.edu",
                                                 "username": "ProfThree", "password": "randompass",
                                                 "phNumber": "5556667777", "mailAdrs": "2 Equalusers Lane",
                                                 "accType": "Professor"
                                                 }, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username",
                         "failed creation. One or more fields invalid")

