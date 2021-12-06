from django.test import TestCase
from DataLog.models import Staff
from django.test import Client

#TODO: add many more fields for creation

#fullName, email, username, password, phNumber, mailAdrs, accType


class TestCreateValid(TestCase):

    def setUp(self):
        client = None
        client = Client()

    #Create TA accounts
    def testGoodCreateTA(self):
        resp = self.client.post("/createuser/", {"fullName" : "nameone", "email" : "test123@gmail.com",
                                                "username": "userone","password": "passone",
                                                "phNumber" : "1234567890", "mailAdrs" : "123 Applesauce Ln.",
                                                "accType" : "TA"
                                                }, follow=True)
        self.assertEqual(resp.context["msg"], "Success: New Account has been create ", "failed creation. One or more fields invalid")

        resp = self.client.post("/createuser/", {"fullName" : "nametwo", "email" : "test345@gmail.com",
                                                "username": "usertwo","password": "passtwo",
                                                "phNumber" : "9999999999", "mailAdrs" : "150 Kenwood Blvd.",
                                                "accType" : "TA"
                                                }, follow=True)
        self.assertEqual(resp.context["msg"], "Success: New Account has been create ", "failed creation. One or more fields invalid")

    #Create professor accounts
    def testGoodCreateProf(self):
        resp = self.client.post("/createuser/", {"fullName" : "profone", "email" : "prof123@gmail.com",
                                                "username": "profusernameone","password": "profpass",
                                                "phNumber" : "1334667999", "mailAdrs" : "7 Professor Circle",
                                                "accType" : "Professor"
                                                }, follow=True)
        self.assertEqual(resp.context['msg'], "Success: New Account has been create ", "failed creation. One or more fields invalid")

        resp = self.client.post("/createuser/", {"fullName" : "proftwo", "email" : "proftwo@gmail.com",
                                                "username": "proftwo","password": "proftwopass",
                                                "phNumber" : "2222222222", "mailAdrs" : "2 Professor way.",
                                                "accType" : "Professor"
                                                }, follow=True)
        self.assertEqual(resp.context['msg'], "Success: New Account has been create ", "failed creation. One or more fields invalid")




class TestCreateInvalid(TestCase):

    def setUp(self):
        client = None
        client = Client()

    def testBlankFields(self):
        #all blank
        resp = self.client.post("/createuser/", {"fullName" : "", "email" : "",
                                                "username": "","password": "",
                                                "phNumber" : "", "mailAdrs" : "",
                                                "accType" : ""
                                                }, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "blank username worked. user: , pass:passone")

    def invalidPhoneNum(self):
        resp = self.client.post("/createuser/", {"fullName": "", "email": "",
                                                 "username": "", "password": "",
                                                 "phNumber": "", "mailAdrs": "",
                                                 "accType": ""
                                                 }, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username",
                         "blank username worked. user: , pass:passone")

        def invalidNameFields(self):
            resp = self.client.post("/createuser/", {"fullName": "", "email": "",
                                                     "username": "", "password": "",
                                                     "phNumber": "", "mailAdrs": "",
                                                     "accType": ""
                                                     }, follow=True)
            self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username",
                             "blank username worked. user: , pass:passone")

    def testDuplicate(self):

        resp = self.client.post("/createuser/", {"username": "userone", "password": "passone"}, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "duplicate user worked. user:userone, pass:passone")

        resp = self.client.post("/createuser/", {"username": "usertwo", "password": "passtwo"}, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "duplicate user worked. user:usertwo, pass:passtwo")

        resp = self.client.post("/createuser/", {"username": "userthree", "password": "passthree"}, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "duplicate user worked. user:userthree, pass:passthree")

