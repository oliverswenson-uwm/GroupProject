from django.test import TestCase
from DataLog.models import *


class test_Archieved_user(TestCase):
    # def setUp(self):
        # self.admin = Admin(name="aasdf", email="adminonetest@gmail.com", username="admin",
        #                    password="admin", phoneNum=9529529952, mailAddress="123 AdminTest Way")
        # self.ta1 = self.admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
        #                                password="testpassoneTA",
        #                                phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")

    def test_regular(self):
        # temp = ArchivedUser.createArchive(self, "TA1", "ta1@ads.com", "ta1", "ta1", "1234", "123st")
        # self.assertEqual(temp.name, "TA1")
        # self.assertEqual(temp.username, "ta1")
        # self.assertEqual(temp.email, "ta1@ads.com")
        # self.assertEqual(temp.password, "ta1")
        # self.assertEqual(temp.phoneNum, "1234")
        # self.assertEqual(temp.mailAddress, "123st")
        self.ta1 = Admin.createTA(fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                                  password="testpassoneTA",
                                  phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        temp = Admin.archiveAccount(self.ta1)
        self.assertEqual(temp.name, self.ta1.name)
