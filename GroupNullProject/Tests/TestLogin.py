from django.test import TestCase, Client
from GroupNullProject.models import *

class SuccessfulLogin(TestCase):

    client = None
    def SetUp(self):
        pass

    def goodLogins(self):
        pass

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
    #TODO potentially change error message

def test_userNotExist(self):
    resp = self.client.post("/", {"name": "userdoesnotexist", "password": "passone"}, follow=True)
    self.assertEqual(resp.context["message"], "user does not exist", "no failed login. user:userdoesnotexist, pass:passone")

def test_noPasswordProvided(self):
    resp = self.client.post("/", {"name": "two", "password": ""}, follow=True)
    self.assertEqual(resp.context["message"], "bad password", "no failed login password, user:one, pass: NULL")

def test_noUserProvided(self):
    resp = self.client.post("/", {"name": "", "password": "two"}, follow=True)
    self.assertEqual(resp.context["message"], "bad password", "no failed login password, user:NULL, pass: two")

def test_twoBlankFields(self):
    pass