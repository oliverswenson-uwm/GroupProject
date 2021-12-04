from django.test import TestCase
from DataLog.models import Staff
from django.test import Client



#no setup becasue creating users on page
class TestCreateValid(TestCase):
    client = None

    def testGoodCreate(TestCase):
    resp = self.client.post("newaccount/", {"name": "userone", "password": "passone"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation successful", "failed creation. user:userone, pass:passone")

    resp = self.client.post("newaccount/", {"name": "usertwo", "password": "passtwo"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation successful", "failed creation. user:usertwo, pass:passtwo")

    resp = self.client.post("newaccount/", {"name": "userthree", "password": "passthree"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation successful", "failed creation. user:userthree, pass:passthree")

class TestCreateInvalid(TestCase):

    #one blank
    resp = self.client.post("newaccount/", {"name": "", "password": "passone"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "blank username worked. user: , pass:passone")

    #one blank
    resp = self.client.post("newaccount/", {"name": "usertwo", "password": ""}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "blank password worked. user:usertwo, pass:")

    #both blank
    resp = self.client.post("newaccount/", {"name": "", "password": ""}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "blank fields worked. user:, pass:")

    #invalid characters
    resp = self.client.post("newaccount/", {"name": "/!#$", "password": "   "}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "invalid tokens worked. user:, pass:")


class TestCreateDuplicate(TestCase):

    def SetUp(self):

        self.client = Client()
        self.userList = {
            "userone": "passone",  # user one
            "usertwo": "passtwo",  # user two
            "userthree": "passthree"  # user three
        }
        for i in self.userList.keys():
            temp = Staff(userName=i, password=userList.get(i))
            print(temp)
            temp.save()  # save in database

    resp = self.client.post("newaccount/", {"name": "userone", "password": "passone"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "duplicate user worked. user:userone, pass:passone")

    resp = self.client.post("newaccount/", {"name": "usertwo", "password": "passtwo"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "duplicate user worked. user:usertwo, pass:passtwo")

    resp = self.client.post("newaccount/", {"name": "userthree", "password": "passthree"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "duplicate user worked. user:userthree, pass:passthree")
