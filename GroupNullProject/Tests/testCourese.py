from django.test import TestCase

from django.test import Client

# Writing test as admin as user which have their name as admin.
# Writing test Course as course database.

class test_noDuplicate(TestCase):
    def setUp(self):
        self.client = Client()
        user = MyUser(name="admin", password="password")
        user.save()

        Course(number="337", credit="4").save()

    def test_defualt(self):
        response = self.client.post

