from django.contrib import messages
from django.test import TestCase
from django.test import Client
from DataLog.models import *


class TestCreateLab(TestCase):
    def setUp(self):
        self.admin = Admin(name="AdminMan", email="admintestaccounttwo@uwm.edu", username="AdminTwo",
                           password="Adminpasstwo", phoneNum="1231231111", mailAddress="123 Admin ln.").save()
        self.course = Course(name="CS361", section="401", credits=3, prereqs="None", description="django").save()
        self.lab = Lab(name="CS361", section="801").save()

    def test_noCourse(self):
        # login first
        self.client.post("", {"username": "AdminTwo", "password": "Adminpasstwo"}, follow=True)
        response = self.client.post('/createlab/', {"nameSel": "CS250-401", "labSec": "811"}, follow=True)
        msgs = response.context['messages']
        error = None
        for msg in msgs:
            # get the first msg
            error = msg.__str__()
            break
        self.assertEqual(error, "Failed to create Lab", msg="Can't create lab without CS250 course being existed")

    def test_existed(self):
        # login first
        self.client.post("", {"username": "AdminTwo", "password": "Adminpasstwo"}, follow=True)
        response = self.client.post('/createlab/', {"nameSel": "CS361-401", "labSec": "801"}, follow=True)
        msgs = response.context['messages']
        error = None
        for msg in msgs:
            # get the first msg
            error = msg.__str__()
            break
        self.assertEqual(error, "Failed to create Lab", msg="Can't create lab, since already existed")

    def test_good(self):
        # login first
        self.client.post("", {"username": "AdminTwo", "password": "Adminpasstwo"}, follow=True)
        response = self.client.post('/createlab/', {"nameSel": "CS361-401", "labSec": "802"}, follow=True)
        msgs = response.context['messages']
        error = None
        for msg in msgs:
            # get the first msg
            error = msg.__str__()
            break
        self.assertEqual(error, "Lab created Successfully!", msg="Lab should have been created")
