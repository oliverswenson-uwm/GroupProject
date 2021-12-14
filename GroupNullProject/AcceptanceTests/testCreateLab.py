from django.contrib import messages
from django.test import TestCase
from django.test import Client
from DataLog.models import *


class TestCreateLab(TestCase):
    def test_error(self):
        Admin(name="AdminMan", email="admintestaccounttwo@uwm.edu", username="AdminTwo", password="Adminpasstwo",
              phoneNum="1231231111", mailAddress="123 Admin ln.").save()
        Course(name="CS250", section="401", credits=3, prereqs="None", description="None").save()
        self.client.post("", {"username": "AdminTwo", "password": "Adminpasstwo"}, follow=True)
        response = self.client.post('/createlab/', {"labName": "CS250", "labSec": "811"}, follow=True)
        msgs = response.context['messages']
        for msg in msgs:
            print(msg)



