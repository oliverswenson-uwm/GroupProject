from DataLog.models import Admin
from django.test import TestCase


# noinspection SpellCheckingInspection
class TestAssignProf(TestCase):

    def setUp(self):
        self.admin = Admin(name="TestAdminone", email="adminonetest@gmail.com", username="adminonetestuser",
                           password="adminpassone", phoneNum=9529529952, mailAddress="123 AdminTest Way")
        self.prof1 = self.admin.createProf(fullName="TestprofOne", email="proftesting1@gmail.com",
                                           username="testprofoneuser",
                                           password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        self.course1 = self.admin.createCourse(nm="MATH240", sec="001", cre="3", pre="None", des="matrices")

    def test_default(self):
        self.assigned = self.admin.assignProf(self.prof1, course=self.course1)
        self.assertEqual(self.assigned.__str__(), "Professor TestprofOne is assigned to course MATH240-001")

    def test_noProfessor(self):
        assigned = self.admin.assignProf(prof=None, course=self.course1)
        self.assertEqual(assigned, None)

    def test_noCourse(self):
        self.assigned = self.admin.assignProf(prof=self.prof1, course=None)
        self.assertEqual(self.assigned, None)

    def test_multipleProf(self):
        self.temp = self.admin.assignProf(prof=self.prof1, course=self.course1)
        self.prof2 = self.admin.createProf(fullName="TestprofTwo", email="proftesting2@gmail.com",
                                           username="testproftwouser",
                                           password="profpasstwo", phNumber=3213213211, mailAdrs="2 Professor St.")
        self.assigned = self.admin.assignProf(prof=self.prof2, course=self.course1)
        self.assertEqual(self.assigned, None)

    def test_duplicateProf(self):
        self.temp = self.admin.assignProf(prof=self.prof1, course=self.course1)
        self.assigned = self.admin.assignProf(prof=self.prof1, course=self.course1)
        self.assertEqual(self.assigned, None)


# noinspection SpellCheckingInspection
class TestAssignTA(TestCase):
    def setUp(self):
        self.admin = Admin(name="TestAdminone", email="adminonetest@gmail.com", username="adminonetestuser",
                           password="adminpassone", phoneNum=9529529952, mailAddress="123 AdminTest Way")
        self.ta1 = self.admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                                       password="testpassoneTA",
                                       phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        self.course1 = self.admin.createCourse(nm="MATH240", sec="001", cre="3", pre="None", des="matrices")

    def test_default(self):
        self.assigned = self.admin.assignTA(ta=self.ta1, course=self.course1)
        self.assertEqual(self.assigned.__str__(), "TA TestTAone is assigned to course MATH240-001")

    def test_noTA(self):
        self.assigned = self.admin.assignTA(ta=None, course=self.course1)
        self.assertEqual(self.assigned, None)

    def test_noLab(self):
        self.assigned = self.admin.assignTA(ta=self.ta1, course=None)
        self.assertEqual(self.assigned, None)

    def test_duplicateTA(self):
        self.temp = self.admin.assignTA(ta=self.ta1, course=self.course1)
        self.assigned = self.admin.assignTA(ta=self.ta1, course=self.course1)
        self.assertEqual(self.assigned, None)
