from django.contrib.auth.models import User
from django.test import TestCase, Client

from DataLog.models import *


class AssignProf(TestCase):

    def setUp(self):
        self.admin = Admin(name="TestAdminone", email="adminonetest@gmail.com", username="adminonetestuser",
                           password="adminpassone", phoneNum=9529529951, mailAddress="123 AdminTest Way")
        self.prof1 = self.admin.createProf(fullName="prof1", email="prof1test@gmail.com",
                                           username="Prof1",
                                           password="profone", phNumber=1231231233, mailAdrs="1 prof St.")
        self.ta1 = self.admin.createTA(fullName="ta1", email="tatest1@gmail.com",
                                       username="TA1",
                                       password="taone", phNumber=1231231233, mailAdrs="1 TA St.")
        self.course1 = self.admin.createCourse(nm="MATH240", sec="101", cre="3", pre="None", des="matrices")
        self.lab1 = self.admin.createLab(name="MATH240", section=801)

        self.ta2 = self.admin.createTA(fullName="ta2", email="tatest2@gmail.com",
                                       username="TA2",
                                       password="tatwo", phNumber=1231231233, mailAdrs="2 TA St.")

    def test_default(self):
        self.client.post("", {"username": "Prof1", "password": "profone"}, follow=True)
        response = self.client.post("/tatoLab/", {"taSel": "ta1-TA1", "labSel": "MATH240-801"}, follow=True)
        msgs = response.context['messages']
        error = None
        for msg in msgs:
            # get the first msg
            error = msg.__str__()
            break
        self.assertEqual(error, "TA assigned", msg="Lab should be created")

    def test_duplicate(self):
        self.client.post("", {"username": "Prof1", "password": "profone"}, follow=True)
        self.client.post("/tatoLab/", {"taSel": "ta2-TA2", "labSel": "MATH240-801"}, follow=True)
        response = self.client.post("/tatoLab/", {"taSel": "ta2-TA2", "labSel": "MATH240-801"}, follow=True)
        msgs = response.context['messages']
        error = None
        for msg in msgs:
            # get the first msg
            error = msg.__str__()
            break
        self.assertEqual(error, "Unable to add Ta to Lab", msg="The ta is already added to the lab")