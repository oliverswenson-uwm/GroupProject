from DataLog.models import Admin, ProfessorToCourse, TAToCourse, TAToLab, Course
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
        self.assigned = self.admin.assignProf(self.prof1.username, self.course1.name, self.course1.section)
        self.assertEqual(self.assigned.__str__(), "Professor TestprofOne is assigned to course MATH240-1")

    def test_noProfessor(self):
        self.assigned = self.admin.assignProf(None, self.course1.name, self.course1.section)
        self.assertEqual(self.assigned, None)

    def test_noCourse(self):
        self.assigned = self.admin.assignProf(self.prof1.username, None, None)
        self.assertEqual(self.assigned, None)

    def test_noCourseSection(self):
        self.assigned = self.admin.assignProf(self.prof1.username, self.course1.name, None)
        self.assertEqual(self.assigned, None)


    def test_multipleProf(self):
        self.temp = self.admin.assignProf(self.prof1.username, self.course1.name, self.course1.section)
        self.prof2 = self.admin.createProf(fullName="TestprofTwo", email="proftesting2@gmail.com",
                                           username="testproftwouser",
                                           password="profpasstwo", phNumber=3213213211, mailAdrs="2 Professor St.")
        self.assigned = self.admin.assignProf(self.prof2.username, self.course1.name, self.course1.section)
        self.assertEqual(self.assigned, None)

    def test_duplicateProf(self):
        self.temp = self.admin.assignProf(self.prof1.username, self.course1.name, self.course1.section)
        self.assigned = self.admin.assignProf(self.prof1.username, self.course1.name, self.course1.section)
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
        self.assigned = self.admin.assignTAToCourse(self.ta1.username, self.course1.name, self.course1.section)
        self.assertEqual(self.assigned.__str__(), "TA TestTAone is assigned to course MATH240-1")

    def test_noTA(self):
        self.assigned = self.admin.assignTAToCourse(None, self.course1.name, self.course1.section)
        self.assertEqual(self.assigned, None)

    def test_noCourse(self):
        self.assigned = self.admin.assignTAToCourse(self.ta1.username, None, None)
        self.assertEqual(self.assigned, None)

    def test_noCourseSection(self):
        self.assigned = self.admin.assignTAToCourse(self.ta1.username, self.course1.name, None)
        self.assertEqual(self.assigned, None)

    def test_multipleTA(self):
        self.temp = self.admin.assignTAToCourse(self.ta1.username, self.course1.name, self.course1.section)
        self.ta2 = self.admin.createTA(fullName="TestTAtwo", email="taTwoGmail1@gmail.com", username="testTAtwo",
                                       password="testpasstwoTA", phNumber=3334441111,
                                       mailAdrs="3 TeachingAssistant Circle")
        self.assigned = self.admin.assignTAToCourse(self.ta2.username, self.course1.name, self.course1.section)
        self.assertEqual(self.assigned, None)

    def test_duplicateTA(self):
        self.temp = self.admin.assignTAToCourse(self.ta1.username, self.course1.name, self.course1.section)
        self.assigned = self.admin.assignTAToCourse(self.ta1.username, self.course1.name, self.course1.section)
        self.assertEqual(self.assigned, None)
