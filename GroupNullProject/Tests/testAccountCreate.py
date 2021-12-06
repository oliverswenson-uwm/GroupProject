from django.test import TestCase
from DataLog.models import Staff
from django.test import Client

client = None
client = Client()

class TestCreateValid(TestCase):


    def testGoodCreate(self):
        resp = self.client.post("newaccount/", {"username": "userone", "password": "passone"}, follow=True)
        self.assertEqual(resp.context['msg'], "Success: New Account has been create ", "failed creation. user:userone, pass:passone")

        resp = self.client.post("newaccount/", {"username": "usertwo", "password": "passtwo"}, follow=True)
        self.assertEqual(resp.context['msg'], "Success: New Account has been create ", "failed creation. user:usertwo, pass:passtwo")

        resp = self.client.post("newaccount/", {"username": "userthree", "password": "passthree"}, follow=True)
        self.assertEqual(resp.context['msg'], "Success: New Account has been create ", "failed creation. user:userthree, pass:passthree")


class TestCreateInvalid(TestCase):

    def testBadCreate(self):
        #one blank
        resp = self.client.post("newaccount/", {"username": "", "password": "passone"}, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "blank username worked. user: , pass:passone")

        #one blank
        resp = self.client.post("newaccount/", {"username": "usertwo", "password": ""}, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "blank password worked. user:usertwo, pass:")

        #both blank
        resp = self.client.post("newaccount/", {"username": "", "password": ""}, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "blank fields worked. user:, pass:")

        #invalid characters
        resp = self.client.post("newaccount/", {"username": "/!#$", "password": "   "}, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "invalid tokens worked. user:, pass:")


class TestCreateDuplicate(TestCase):

    def testDuplicate(self):


        resp = self.client.post("newaccount/", {"username": "userone", "password": "passone"}, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "duplicate user worked. user:userone, pass:passone")

        resp = self.client.post("newaccount/", {"username": "usertwo", "password": "passtwo"}, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "duplicate user worked. user:usertwo, pass:passtwo")

        resp = self.client.post("newaccount/", {"username": "userthree", "password": "passthree"}, follow=True)
        self.assertEqual(resp.context['msg'], "Fail: Username exist, Please Pick a new Username", "duplicate user worked. user:userthree, pass:passthree")
