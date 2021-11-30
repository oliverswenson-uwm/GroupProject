from django.test import TestCase, Client
from GroupNullProject.models import User

class SuccessFulLogin(TestCase):
    pass

class FailedLogin(TestCase):

    client = None

    def setUp(self):
        self.client = Client()
        self.userList = {
            "userone": "passone",
            "usertwo": "passtwo",
            "userthree": "passthree"
        }

        for i in self.userList.keys():

            temp = MyUser(name=i, password=i)
            print(temp)
            #temp.save()#save in database

        for j in self.userList[i]:
            Stuff(name=j, owner=temp).save()


def test_badPasswordProvided(self):
    resp = self.client.post("/", {"name": "one", "password": "three"}, follow=True)
    self.assertEqual(resp.context["message"], "bad password", "no failed login password, user:one, pass:three")


def test_OtherUserPassword(self):
    resp = self.client.post("/", {"name": "one", "password": "two"}, follow=True)
    self.assertEqual(resp.context["message"], "bad password",
                     "no failed login password, user:one, pass:two, two is valid for another user")


def test_noPasswordProvided(self):
    resp = self.client.post("/", {"name": "two", "password": ""}, follow=True)
    self.assertEqual(resp.context["message"], "bad password", "no failed login password, user:one, pass: NULL")


def test_noUserProvided(self):
    resp = self.client.post("/", {"name": "", "password": "two"}, follow=True)
    self.assertEqual(resp.context["message"], "bad password", "no failed login password, user:NULL, pass: two")