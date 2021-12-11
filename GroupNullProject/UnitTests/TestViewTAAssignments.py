from django.test import TestCase

from DataLog.models import Admin


class TestViewTAAssignments(TestCase):
    def setUp(self):
        self.admin = Admin(fullName="TestAdminOne", email="adminonetest@gmail.com", username="adminonetestuser",
                           password="adminpassone", phNumber=9529529952, mailAdrs="123 AdminTest Way")
        self.ta1 = self.admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                                       password="testpassoneTA",
                                       phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        self.lab1 = self.admin.createLab(name="Math240", section="000")
        self.course1 = self.admin.createCourse(nm="MATH240", sec="001", cre="3", pre="None", des="matrices")
        self.admin.assignTA(ta=self.ta1, lab=self.lab1)

    def test_default(self):
        assignments = self.ta1.viewAssignments()
        self.assertEqual(assignments.ta1, "TestTAone")
        self.assertEqual(assignments.course, "MATH240")
        self.assertEqual(assignments.section, "000")

    def test_noAssignments(self):
        ta2 = self.admin.createTA(fullName="TestTAtwo", email="taTwoGmail1@gmail.com", username="testTAtwo",
                                  password="testpasstwoTA", phNumber=1111111111, mailAdrs="3 TeachingAssistant Circle")
        self.assertEqual(ta2.viewAssignments(), None)
