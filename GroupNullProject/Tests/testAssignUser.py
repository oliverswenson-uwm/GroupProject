from django.contrib.auth.models import User
from django.test import TestCase, Client

from DataLog.models import Staff, Admin, Professor, TA, Course, Lab, LabToCourse, ProfessorToCourse, TAToCourse, TAToLab


class AssignUser(TestCase):

    def SetUp(self):
        self.client = Client()
        Professor(name="Prof", email="a@uwm.edu", username="assign",
                  password="123", phoneNum="123", mailAddress="123").save()
        TA(name="TA", email="t@uwm.edu", username="TA", password="123", phoneNum="123", mailAddress="123").save()
        Course(name="MATH240", section="001", credits="3", prereqs="MATH101",
               description="Matrices").save()

    def test_default(self):
        response = self.client.post('/assignuser/', {"cnum": "MATH240", "csec": "001", "usern": "assign"}, follow=True)
        self.assertEqual("assign", response.context["usern"])
        self.assertEqual("MATH240", response.context["cnum"])
        self.assertEqual("001", response.context["csec"])

    def test_invalidUser(self):
        response = self.client.post('/assignuser/', {"cnum": "MATH240", "csec": "001", "usern": "invalid"}, follow=True)
        self.assertEqual("Invalid Username", response.context['msg'])

    def test_inValidCourse(self):
        response = self.client.post('/assignuser/', {"cnum": "COMPSCI240", "csec": "001", "usern": "assign"}, follow=True)
        self.assertEqual("Invalid course number or section", response.context['msg'])

    def test_assignIncorrectSection(self):
        response = self.client.post('/assignuser/', {"cnum": "MATH240", "csec": "000", "usern": "TA"},
                                    follow=True)
        self.assertEqual("Invalid course number or section", response.context['msg'])


class testDuplicates(TestCase):
    def SetUp(self):
        self.client = Client()
        prof = Professor(name="Prof2", email="b@uwm.edu", username="assign2",
                         password="123", phoneNum="123", mailAddress="123").save()
        Professor(name="Prof", email="a@uwm.edu", username="assign",
                  password="123", phoneNum="123", mailAddress="123").save()
        ta = TA(name="TA", email="t@uwm.edu", username="TA", password="123", phoneNum="123", mailAddress="123").save()
        course = Course(name="MATH240", section="001", credits="3", prereqs="MATH101",
                        description="Matrices").save()
        Course(name="MATH240", section="000", credits="3", prereqs="MATH101",
               description="Matrices").save()

        ProfessorToCourse.objects.create(professor=prof, course=course)
        TAToCourse.objects.create(ta=ta, course=course)

    def test_assignDuplicateToCourse(self):
        response = self.client.post('/assignuser/', {"cnum": "MATH240", "csec": "001", "usern": "assign"},
                                    follow=True)
        self.assertEqual("Professor already assigned to course", response.context['msg'])

    def test_assignMultipleProfessors(self):
        response = self.client.post('/assignuser/', {"cnum": "MATH240", "csec": "001", "usern": "assign2"},
                                    follow=True)
        self.assertEqual("A different Professor is already assigned to course", response.context['msg'])

    def test_assignDuplicateToSection(self):
        response = self.client.post('/assignuser/', {"cnum": "MATH240", "csec": "001", "usern": "TA"},
                                    follow=True)
        self.assertEqual("TA already assigned to section", response.context['msg'])

    def test_assignMultipleSections(self):
        response = self.client.post('/assignuser/', {"cnum": "MATH240", "csec": "000", "usern": "TA"},
                                    follow=True)
        self.assertEqual("TA already assigned to a different section", response.context['msg'])
