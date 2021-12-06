from django.test import TestCase, Client
from DataLog.models import Staff, Admin, Professor, TA, Course, Lab, LabToCourse, ProfessorToCourse, TAToCourse, TAToLab


class SuccessfulLogin(TestCase):

    def setUp(self):
        client = None
        self.client = Client()

    def goodLoginOne(self):
        resp = self.client.post("/", {"username": "userone", "password": "passone"}, follow=True)
        self.assertEqual(resp.context["msg"], "login successful", "failed login. user:userone, pass:passone")

    def goodLoginTwo(self):
        resp = self.client.post("/", {"username": "usertwo", "password": "passtwo"}, follow=True)
        self.assertEqual(resp.context["msg"], "login successful", "failed login. user:usertwo, pass:passtwo")

    def goodLoginThree(self):
        resp = self.client.post("/", {"username": "userthree", "password": "passthree"}, follow=True)
        self.assertEqual(resp.context["msg"], "INVALID Username OR Password", "failed login. user:userthree, pass:passthree")

class FailedLogin(TestCase):

    def setUp(self):
        client = None
        self.client = Client()

    def test_passwordNotMatch(self):
        resp = self.client.post("/", {"username": "userone", "password": "passtwo"}, follow=True)
        self.assertEqual(resp.context["msg"], "INVALID Username OR Password", "no failed login. user:userone, pass:passtwo")

    def test_userNotExist(self):
        resp = self.client.post("/", {"username": "userdoesnotexist", "password": "passone"}, follow=True)
        self.assertEqual(resp.context["msg"], "INVALID Username OR Password", "no failed login. user:userdoesnotexist, pass:passone")

    def test_noPasswordProvided(self):
        resp = self.client.post("/", {"username": "userone", "password": ""}, follow=True)
        self.assertEqual(resp.context["msg"], "INVALID Username OR Password", "no failed login. user:userone, pass: NULL")

    def test_noUserProvided(self):
        resp = self.client.post("/", {"username": "", "password": "passthree"}, follow=True)
        self.assertEqual(resp.context["msg"], "INVALID Username OR Password", "no failed login. user:NULL, pass: passthree")

    def test_twoBlankFields(self):
        resp = self.client.post("/", {"username": "", "password": ""}, follow=True)
        self.assertEqual(resp.context["msg"], "INVALID Username OR Password", "no failed login. user:NULL, pass: NULL")
