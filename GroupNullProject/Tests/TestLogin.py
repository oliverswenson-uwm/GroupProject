from django.test import TestCase, Client
from GroupNullProject.models import *

class SuccessfulLogin(TestCase):

    client = None
    def SetUp(self):
        self.client = Client()
        self.userList = {
            "userone": "passone", #user one
            "usertwo": "passtwo", #user two
            "userthree": "passthree" #user three
        }
        for i in self.userList.keys():
            temp = MyUser(name=i, password = userList.get(i))
            print(temp)
            temp.save() #save in database

    def goodLoginOne(self):
        resp = self.client.post("/", {"name": "userone", "password": "passone"}, follow=True)
        self.assertEqual(resp.context["message"], "login successful", "failed login. user:userone, pass:passone")
        # potentially change error message

    def goodLoginTwo(self):
        resp = self.client.post("/", {"name": "usertwo", "password": "passtwo"}, follow=True)
        self.assertEqual(resp.context["message"], "login successful", "failed login. user:usertwo, pass:passtwo")
        # potentially change error message

    def goodLoginThree(self):
        resp = self.client.post("/", {"name": "userthree", "password": "passthree"}, follow=True)
        self.assertEqual(resp.context["message"], "bad password", "failed login. user:userthree, pass:passthree")
        # potentially change error message

class FailedLogin(TestCase):
    client = None
    def setUp(self):
        self.client = Client()
        self.userList = {
            "userone": "passone", #user one
            "usertwo": "passtwo", #user two
            "userthree": "passthree" #user three
        }
        for i in self.userList.keys():
            temp = MyUser(name=i, password = userList.get(i))
            print(temp)
            temp.save() #save in database

def test_passwordNotMatch(self):
    resp = self.client.post("/", {"name": "userone", "password": "passtwo"}, follow=True)
    self.assertEqual(resp.context["message"], "bad password", "no failed login. user:userone, pass:passtwo")
    #potentially change error message

def test_userNotExist(self):
    resp = self.client.post("/", {"name": "userdoesnotexist", "password": "passone"}, follow=True)
    self.assertEqual(resp.context["message"], "user does not exist", "no failed login. user:userdoesnotexist, pass:passone")
    # potentially change error message

def test_noPasswordProvided(self):
    resp = self.client.post("/", {"name": "userone", "password": ""}, follow=True)
    self.assertEqual(resp.context["message"], "no password provided", "no failed login. user:userone, pass: NULL")
    # potentially change error message

def test_noUserProvided(self):
    resp = self.client.post("/", {"name": "", "password": "passthree"}, follow=True)
    self.assertEqual(resp.context["message"], "no username provided", "no failed login. user:NULL, pass: passthree")
    # potentially change error message

def test_twoBlankFields(self):
    resp = self.client.post("/", {"name": "", "password": ""}, follow=True)
    self.assertEqual(resp.context["message"], "no username or password provided", "no failed login. user:NULL, pass: NULL")
    # potentially change error message