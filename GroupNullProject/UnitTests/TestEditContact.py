from django.test import TestCase
from DataLog.models import *

class TestEditContact(TestCase):
    # PBI says that the professors and TAs can edit their contact information EXCEPT for their emails.
    def testEditPhone(self):
        # First form of contact info is the phone number
        Admin.createProf(self, fullName= "Ron Ronald", email= "ronsquared@gmail.com", username= "rooon",
                        password= "ronword", phNumber= 2222233333, mailAdrs= "123 AdminTest Way")

        dummyAcc, editedUser = Staff.getUser(self, "adminonetestuser")
        editedUser.EditContact(self, 1111199999, "123 AdminTest Way")

        self.assertEqual(editedUser.phNumber, 1111199999)

    def testEditAddress(self):
        # Second form of contact info is the mailing address
        Admin.createProf(self, fullName= "Ron Ronald", email= "ronsquared@gmail.com", username= "rooon",
                        password= "ronword", phNumber= 2222233333, mailAdrs= "123 AdminTest Way")

        dummyAcc, editedUser = Staff.getUser(self, "Ron Ronald")
        editedUser.EditContact(self, 2222233333, "444 Changestreet Boulevard")

        self.assertEqual(editedUser.mailAdrs, "444 Changestreet Boulevard")

class TestErrorEdits(TestCase):
    # This test class is for the negative/error cases that could occur when editing the specific fields.
    # First test is if they enter a phone number as letters
    def testTextPhone(self):
        with self.assertRaises(TypeError, msg="Your phone number shouldn't be in letters. Use numbers!"):
            Admin.createProf(self, fullName="Ron Ronald", email="ronsquared@gmail.com", username="rooon",
                             password="ronword", phNumber=2222233333, mailAdrs="123 AdminTest Way")

            dummyAcc, editedUser = Staff.getUser(self, "Ron Ronald")
            editedUser.EditContact(self, "two two two three three three", "444 Changestreet Boulevard")

            self.assertEqual(editedUser.phNumber, "two two two three three three")

    def testIntegerAddress(self):
        with self.assertRaises(TypeError, msg="Your mailing address shouldn't be in integers. Use letters!"):
            Admin.createProf(self, fullName="Ron Ronald", email="ronsquared@gmail.com", username="rooon",
                             password="ronword", phNumber=2222233333, mailAdrs="123 AdminTest Way")

            dummyAcc, editedUser = Staff.getUser(self, "Ron Ronald")
            editedUser.EditContact(self, 2222233333, 44442100120021)

            self.assertEqual(editedUser.mailAdrs, 44442100120021)