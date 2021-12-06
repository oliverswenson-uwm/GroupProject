from django.test import TestCase
from DataLog.models import Staff
from django.test import Client



class TestCreateValid(TestCase):
    client = None

    def testGoodCreate(TestCase):
    resp = self.client.post("newaccount/", {"username": "userone", "password": "passone"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation successful", "failed creation. user:userone, pass:passone")

    resp = self.client.post("newaccount/", {"username": "usertwo", "password": "passtwo"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation successful", "failed creation. user:usertwo, pass:passtwo")

    resp = self.client.post("newaccount/", {"username": "userthree", "password": "passthree"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation successful", "failed creation. user:userthree, pass:passthree")


class TestCreateInvalid(TestCase):

    #one blank
    resp = self.client.post("newaccount/", {"username": "", "password": "passone"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "blank username worked. user: , pass:passone")

    #one blank
    resp = self.client.post("newaccount/", {"username": "usertwo", "password": ""}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "blank password worked. user:usertwo, pass:")

    #both blank
    resp = self.client.post("newaccount/", {"username": "", "password": ""}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "blank fields worked. user:, pass:")

    #invalid characters
    resp = self.client.post("newaccount/", {"username": "/!#$", "password": "   "}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "invalid tokens worked. user:, pass:")


class TestCreateDuplicate(TestCase):

    self.client = Client()

    resp = self.client.post("newaccount/", {"username": "userone", "password": "passone"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "duplicate user worked. user:userone, pass:passone")

    resp = self.client.post("newaccount/", {"username": "usertwo", "password": "passtwo"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "duplicate user worked. user:usertwo, pass:passtwo")

    resp = self.client.post("newaccount/", {"username": "userthree", "password": "passthree"}, follow=True)
    self.assertEqual(resp.context["message"], "account creation failed", "duplicate user worked. user:userthree, pass:passthree")
