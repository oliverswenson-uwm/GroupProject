from django.test import TestCase, Client
from DataLog.models import Staff, Admin, Professor, TA


class SuccessfulLogin(TestCase):

    def setUp(self):
        client = None
        self.client = Client()
        #create one account of each type to test
        TA(name="TA", email="tatestone@uwm.edu", username="TAone", password="TApassone", phoneNum="1111119111",mailAddress="123 TA ln.").save()
        Admin(name="AdminMan", email="admintestaccounttwo@uwm.edu", username="AdminTwo", password="Adminpasstwo", phoneNum="1231231111", mailAddress="123 Admin ln.").save()
        Professor(name="ProfessorMan", email="profthree@uwm.edu", username="ProfThree", password="Profpassthree",phoneNum="1234567777", mailAddress="123 Professor ln.").save()

    #TA login, checking if redirect sent 200 OK code
    def test_goodLoginOne(self):
        resp = self.client.post("", {"username": "TAone", "password": "TApassone"}, follow=True)
        self.assertEqual(resp.status_code, 200)

    #admin login, checking if http respose is a redirect (dont follow)
    def test_goodLoginTwo(self):
        resp = self.client.post("", {"username": "AdminTwo", "password": "Adminpasstwo"}, follow=False)
        self.assertEqual(resp.status_code, 302)

    # professor login, checking if redirect sent 200 OK code after folloring
    def test_goodLoginThree(self):
        resp = self.client.post("", {"username": "ProfThree", "password": "Profpassthree"}, follow=True)
        self.assertEqual(resp.status_code, 200)


class FailedLogin(TestCase):

    def setUp(self):
        client = None
        self.client = Client()
        #create one account of each type to test
        TA(name="TA", email="tatestone@uwm.edu", username="TAone", password="TApassone", phoneNum="1111119111",mailAddress="123 TA ln.").save()
        Admin(name="AdminMan", email="admintestaccounttwo@uwm.edu", username="AdminTwo", password="Adminpasstwo",phoneNum="1231231111", mailAddress="123 Admin ln.").save()
        Professor(name="ProfessorMan", email="profthree@uwm.edu", username="ProfThree", password="Profpassthree",phoneNum="1234567777", mailAddress="123 Professor ln.").save()

    def test_passwordNotMatch(self):
        resp = self.client.post("", {"username": "userone", "password": "passtwo"}, follow=True)
        self.assertEqual(resp.context['msg'], "INVALID Username OR Password",
                         "no failed login. user:userone, pass:passtwo")

    def test_userNotExist(self):
        resp = self.client.post("", {"username": "userdoesnotexist", "password": "passone"}, follow=True)
        self.assertEqual(resp.context['msg'], "INVALID Username OR Password",
                         "no failed login. user:userdoesnotexist, pass:passone")

    def test_noPasswordProvided(self):
        resp = self.client.post("", {"username": "userone", "password": ""}, follow=True)
        self.assertEqual(resp.context['msg'], "INVALID Username OR Password",
                         "no failed login. user:userone, pass: NULL")

    def test_noUserProvided(self):
        resp = self.client.post("", {"username": "", "password": "passthree"}, follow=True)
        self.assertEqual(resp.context['msg'], "INVALID Username OR Password",
                         "no failed login. user:NULL, pass: passthree")

    def test_twoBlankFields(self):
        resp = self.client.post("", {"username": "", "password": ""}, follow=True)
        self.assertEqual(resp.context['msg'], "INVALID Username OR Password", "no failed login. user:NULL, pass: NULL")
