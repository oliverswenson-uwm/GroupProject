from django.contrib.auth.models import User
from django.test import TestCase, Client

from DataLog.models import Staff, Admin, Professor, TA, Course, Lab, LabToCourse, ProfessorToCourse, TAToCourse, TAToLab


class AssignProf(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin = Admin(name="TestAdminone", email="adminonetest@gmail.com", username="adminonetestuser",
                           password="adminpassone", phoneNum=9529529951, mailAddress="123 AdminTest Way")
        self.prof1 = self.admin.createProf(fullName="TestprofOne", email="proftesting1@gmail.com",
                                           username="testprofoneuser",
                                           password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        self.course1 = self.admin.createCourse(nm="MATH240", sec="101", cre="3", pre="None", des="matrices")

    def test_default(self):
        resp = self.client.post("/assignprof/", {"profSel": "TestprofOne-testprofoneuser",
                                                 "courseSel": "MATH240-101"
                                                 }, follow=True)
        msgs = resp.context['messages']
        error = None
        for msg in msgs:
            # get the first msg
            error = msg.__str__()
            break
        self.assertEqual(error, "Professor assigned", msg="Professor assigned successfully")

    def test_duplicate(self):
        self.temp = self.admin.assignProf(self.prof1.username, self.course1.name, self.course1.section)
        resp = self.client.post("/assignprof/", {"profSel": "TestprofOne-testprofoneuser",
                                                 "courseSel": "MATH240-101"
                                                 }, follow=True)
        msgs = resp.context['messages']
        error = None
        for msg in msgs:
            # get the first msg
            error = msg.__str__()
            break
        self.assertEqual(error, "Unable to add professor to Course", msg="Professor already assigned to course")

    def test_multiple(self):
        self.admin.assignProf(self.prof1.username, self.course1.name, self.course1.section)
        self.prof1 = self.admin.createProf(fullName="TestprofTwo", email="proftesting2@gmail.com",
                                           username="testproftwouser",
                                           password="profpasstwo", phNumber=2231231233, mailAdrs="2 Professor St.")
        resp = self.client.post("/assignprof/", {"profSel": "TestprofTwo-testproftwouser",
                                                 "courseSel": "MATH240-101"
                                                 }, follow=True)
        msgs = resp.context['messages']
        error = None
        for msg in msgs:
            # get the first msg
            error = msg.__str__()
            break
        self.assertEqual(error, "Unable to add professor to Course", msg="Course already has a professor")


class assignTaToCourse(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = Admin(name="TestAdminone", email="adminonetest@gmail.com", username="adminonetestuser",
                           password="adminpassone", phoneNum=9529529951, mailAddress="123 AdminTest Way")
        self.ta1 = self.admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAoneuser",
                                       password="testpassoneTA",
                                       phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        self.course1 = self.admin.createCourse(nm="MATH240", sec="101", cre="3", pre="None", des="matrices")

    def test_default(self):
        resp = self.client.post("/tatocourse/", {"taSel": "TestTAone-testTAoneuser",
                                                 "courseSel": "MATH240-101"
                                                 }, follow=True)
        msgs = resp.context['messages']
        error = None
        for msg in msgs:
            # get the first msg
            error = msg.__str__()
            break
        self.assertEqual(error, "TA assigned", msg="TA assigned successfully")

    def test_duplicate(self):
        self.admin.assignTAToCourse(self.ta1.username, self.course1.name, self.course1.section)
        resp = self.client.post("/tatocourse/", {"taSel": "TestTAone-testTAoneuser",
                                                 "courseSel": "MATH240-101"
                                                 }, follow=True)
        msgs = resp.context['messages']
        error = None
        for msg in msgs:
            # get the first msg
            error = msg.__str__()
            break
        self.assertEqual(error, "Unable to add TA to Course", msg="TA already assigned to course")
