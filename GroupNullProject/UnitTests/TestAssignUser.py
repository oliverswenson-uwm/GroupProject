from DataLog.models import Admin
from django.test import TestCase


class TestAssignProf(TestCase):
    def setUP(self):
        self.admin = Admin(fullName="TestAdminone", email="adminonetest@gmail.com", username="adminonetestuser",
                           password="adminpassone", phNumber=9529529952, mailAdrs="123 AdminTest Way")
        self.prof1 = self.admin.createProf(fullName="TestprofOne", email="proftesting1@gmail.com",
                                           username="testprofoneuser",
                                           password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        self.course1 = self.admin.createCourse(nm="MATH240", sec="001", cre="3", pre="None", des="matrices")

    def test_default(self):
        assigned = self.admin.assignProf(prof=self.prof1, course=self.course1)
        self.assertEqual(assigned, "Professor TestprofOne is assigned to course MATH240-001")

    def test_noProfessor(self):
        assigned = self.admin.assignProf(prof=None, course=self.course1)
        self.assertEqual(assigned, None)

    def test_noCourse(self):
        assigned = self.admin.assignProf(prof=self.prof1, course=None)
        self.assertEqual(assigned, None)

    def test_duplicateProf(self):
        self.admin.assignProf(prof=self.prof1, course=self.course1)
        prof2 = self.admin.createProf(fullName="TestprofTwo", email="proftesting2@gmail.com",
                                      username="testproftwouser",
                                      password="profpasstwo", phNumber=3213213211, mailAdrs="2 Professor St.")
        assigned = self.admin.assignProf(prof=prof2, course=self.course1)
        self.assertEqual(assigned, None)


class TestAssignTA(TestCase):
    def setUP(self):
        self.admin = Admin(fullName="TestAdminone", email="adminonetest@gmail.com", username="adminonetestuser",
                           password="adminpassone", phNumber=9529529952, mailAdrs="123 AdminTest Way")
        self.ta1 = self.admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                                       password="testpassoneTA",
                                       phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        self.lab1 = self.admin.createLab(name="Math240", section="000")

    def test_default(self):
        assigned = self.admin.assignTA(ta=self.ta1, lab=self.lab1)
        self.assertEqual(assigned, "TA TestTAone is assigned to lab ")

    def test_noTA(self):
        assigned = self.admin.assignTA(ta=None, lab=self.lab1)
        self.assertEqual(assigned, None)

    def test_noLab(self):
        assigned = self.admin.assignTA(ta=self.ta1, lab=None)
        self.assertEqual(assigned, None)

    def test_duplicateTA(self):
        self.admin.assignTA(ta=self.ta1, lab=self.lab1)
        ta2 = self.admin.createTA(fullName="TestTAtwo", email="taTwoGmail1@gmail.com", username="testTAtwo",
                                  password="testpasstwoTA", phNumber=1111111111, mailAdrs="3 TeachingAssistant Circle")
        assigned = self.admin.assignTA(ta=ta2, lab=self.lab1)
        self.assertEqual(assigned, None)

    def test_multipleLabs(self):
        self.admin.assignTA(ta=self.ta1, lab=self.lab1)
        lab2 = self.admin.createLab(name="Math240", section=100)
        assigned = self.admin.assignTA(ta=self.ta1, lab=lab2)
        self.assertEqual(assigned, None)
