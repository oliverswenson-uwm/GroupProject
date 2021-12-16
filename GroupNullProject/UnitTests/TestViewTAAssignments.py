from django.test import TestCase

from DataLog.models import Admin, Professor


class TestViewTAAssignments(TestCase):
    def setUp(self):
        self.admin = Admin(name="TestAdminone", email="adminonetest@gmail.com", username="adminonetestuser",
                           password="adminpassone", phoneNum=9529529951, mailAddress="123 AdminTest Way")
        self.ta1 = self.admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                                       password="testpassoneTA",
                                       phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        self.course1 = self.admin.createCourse(nm="MATH240", sec="001", cre="3", pre="None", des="matrices")
        self.lab1 = self.admin.createLab(name="MATH240", section="002")
        self.temp = Professor.add_taLab(ta=self.ta1, lab=self.lab1)

    def test_default(self):
        self.assignments = self.ta1.viewAssignments()
        self.assertEqual(self.assignments, [(self.lab1, self.course1)])

    def test_noAssignments(self):
        self.ta2 = self.admin.createTA(fullName="TestTAtwo", email="taTwoGmail1@gmail.com", username="testTAtwo",
                                  password="testpasstwoTA", phNumber=1111111111, mailAdrs="3 TeachingAssistant Circle")
        self.assertEqual(self.ta2.viewAssignments(), None)
