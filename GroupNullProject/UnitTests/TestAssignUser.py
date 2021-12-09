from DataLog.models import Admin
from django.test import TestCase


class TestAssignProf(TestCase):
    def test_default(self):
        prof1 = Admin.createProf(self, fullName="TestprofOne", email="proftesting1@gmail.com",
                                 username="testprofoneuser",
                                 password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        course1 = Admin.createCourse(self, nm="MATH240", sec="001", cre="3", pre="None", des="matrices")
        assigned = Admin.assignProf(prof1, course1)
        self.assertEqual(assigned, "Professor TestprofOne is assigned to course MATH240-001")

    def test_noProfessor(self):
        course1 = Admin.createCourse(self, nm="MATH240", sec="001", cre="3", pre="None", des="matrices")
        assigned = Admin.assignProf(None, course1)
        self.assertEqual(assigned, None)

    def test_noCourse(self):
        prof1 = Admin.createProf(self, fullName="TestprofOne", email="proftesting1@gmail.com",
                                 username="testprofoneuser",
                                 password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        assigned = Admin.assignProf(prof1, None)
        self.assertEqual(assigned, None)


class TestAssignTA(TestCase):

    def test_default(self):
        ta1 = Admin.createTA(self, fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA", phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        lab1 = Admin.createLab(self)  # need createLab() to be done
        assigned = Admin.assignTA(ta1, lab1)
        self.assertEqual(assigned, "TA TestTAone is assigned to lab ")  # needs createLab() to be done

    def test_noTA(self):
        lab1 = Admin.createLab(self)  # need createLab() to be done
        assigned = Admin.assignTA(None, lab1)
        self.assertEqual(assigned, None)

    def tets_noLab(self):
        ta1 = Admin.createTA(self, fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                             password="testpassoneTA", phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        assigned = Admin.assignTA(ta1, None)
        self.assertEqual(assigned, None)
