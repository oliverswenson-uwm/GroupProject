from django.test import TestCase
from DataLog.models import *

class TestEditAcc(TestCase):

    def testEditFullName(self):
        # This test is for changing the name of an account
        Admin.createAdmin(self, fullName = "Tam Sin", email = "tamsin@gmail.com", username = "tsin",
                          password = "101", phNumber = 4444444444, mailAdrs = "123 Wowee Way")
        editedUser = Staff.getUser(self, "adminonetestuser")
        prevUser = Staff.getUser(self, "adminonetestuser")

        editedUser.EditAcc(self, "Tam Sinny", "tamsin@gmail.com", "tsin", "101", 4444444444, "123 Wowee Way")

        self.assertEqual(editedUser.fullName, "Tam Sinny")

    def testEditEmail(self):
        # This test is for changing the email
        Admin.createTA(self, fullName="Sam Tin", email="samtin@gmail.com", username="stin",
                          password="101", phNumber=4444444444, mailAdrs="123 Wowee Way")
        editedUser, prevUser = Staff.getUser(self, "adminonetestuser")

        editedUser.EditAcc(self, "Sam Tin", "sammytin@gmail.com", "stin", "101", 4444444444, "123 Wowee Way")

        self.assertEqual(editedUser.email, "sammytin@gmail.com")

    def testEditUsername(self):
        # This test is for changing the name of an account
        Admin.createAdmin(self, fullName="Tam Sin", email="tamsin@gmail.com", username="tsin",
                          password="101", phNumber=4444444444, mailAdrs="123 Wowee Way")
        editedUser, prevUser = Staff.getUser(self, "adminonetestuser")

        editedUser.EditAcc(self, "Tam Sinny", "tamsin@gmail.com", "strangename", "101", 4444444444, "123 Wowee Way")

        self.assertEqual(editedUser.username, "strangename")

    def testEditPassword(self):
        # This test is for changing the name of an account
        Admin.createAdmin(self, fullName="Tam Sin", email="tamsin@gmail.com", username="tsin",
                          password="101", phNumber=4444444444, mailAdrs="123 Wowee Way")
        editedUser, prevUser = Staff.getUser(self, "adminonetestuser")

        editedUser.EditAcc(self, "Tam Sinny", "tamsin@gmail.com", "tsin", "secure", 4444444444, "123 Wowee Way")

        self.assertEqual(editedUser.password, "secure")

    def testEditPh(self):
        # This test is for changing the name of an account
        Admin.createAdmin(self, fullName="Tam Sin", email="tamsin@gmail.com", username="tsin",
                          password="101", phNumber=4444444444, mailAdrs="123 Wowee Way")
        editedUser, prevUser = Staff.getUser(self, "adminonetestuser")

        editedUser.EditAcc(self, "Tam Sinny", "tamsin@gmail.com", "tsin", "101", 1111144444, "123 Wowee Way", "Professor")

        self.assertEqual(editedUser.phNumber, 1111144444)

    def testEditAdrs(self):
        # This test is for changing the name of an account
        Admin.createAdmin(fullName="Tam Sin", email="tamsin@gmail.com", username="tsin",
                          password="101", phNumber=4444444444, mailAdrs="123 Wowee Way")
        editedUser, prevUser = Staff.getUser(self, "adminonetestuser")

        editedUser.EditAcc(self, "Tam Sinny", "tamsin@gmail.com", "tsin", "101", 4444444444, "Rock Bottom", "TA")

        self.assertEqual(editedUser.mailAdrs, "Rock Bottom")

class TestBadEditAcc(TestCase):
    def testEditBadUsername(self):
        # This is for a possible error when editing an account
        # ie: changing the username to a single integer
        with self.assertRaises(TypeError, msg="You are trying to make a username that is only integers!"):
            Admin.createProf(self, fullName="Professor Slate", email="wahoo@gmail.com", username="profslate",
                            password="101", phNumber=4444444114, mailAdrs="122 Wowee Way")
            editedUser, prevUser = Staff.getUser(self, "adminonetestuser")

            editedUser.EditAcc(self, "Professor Slate", "wahoo@gmail.com", "1", "101", 4444444114, "122 Wowee Way")

            self.assertEqual(editedUser.username, 1)

    def testEditBadEmail(self):
        # This is for a possible error when editing an email
        # ie: No valid email is just an integer
        with self.assertRaises(TypeError, msg="You need a valid email. Just integers is not valid."):
            Admin.createProf(self, fullName="Professor Slate", email="wow@gmail.com", username="profslate",
                            password="101", phNumber=4444444114, mailAdrs="122 Wowee Way")
            editedUser, prevUser = Staff.getUser(self, "adminonetestuser")

            editedUser.EditAcc(self, "Professor Slate", 12234, "1", "101", 4444444114, "122 Wowee Way")

            self.assertEqual(editedUser.email, 12234)

    def testEditBadPassword(self):
        # This is for a possible error when editing and the password field is blank
        # ie: changing the username to a single integer
        with self.assertRaises(TypeError, msg="Your new password is blank!"):
            Admin.createProf(self, fullName="Professor Slate", email="wahoo@gmail.com", username="profslate",
                            password="wahoo", phNumber=4444444114, mailAdrs="122 Wowee Way")
            editedUser, prevUser = Staff.getUser(self, "adminonetestuser")

            editedUser.EditAcc(self, "Professor Slate", "wahoo@gmail.com", "profslate", "", 4444444114, "122 Wowee Way")

            self.assertEqual(editedUser.password, "")