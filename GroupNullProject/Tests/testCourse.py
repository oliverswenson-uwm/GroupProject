from django.test import TestCase

from django.test import Client

from GroupNullProject.models import *


# Writing test as admin as user which have their name as admin.
# Writing test Course as course database.

class test_noDuplicate(TestCase):
    def setUp(self):
        self.client = Client()
        user = User(name="admin", password="password")
        user.save()

        Course(number="337", credit="4").save()

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new courses by entering the course number, credits,
    # prerequisites, and a course description.
    # Then: The course is created at page.

    def test_defualt(self):
        response = self.client.post('/course/', {"number": "MATH231", "credit": "3"}, follow=True)
        self.assertEqual("100", response.context["course"])
        self.assertEqual("3", response.context["credit"])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course using only alphabets on course number.
    # Then: The system does not create course.
    # And: The system displays the course number can't be using only alphabets.
    def test_invalidCourseNumber(self):
        response = self.client.post('/course/', {"number": "abc", "credit": "3"}, follow=True)
        self.assertEqual("The course number cannot be using only alphabets.", response.context["message"])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course by using alphabets on credits.
    # Then: The system does not create course.
    # And: The system displays the course credits can't be using alphabets.
    def test_invalidCourseCredit(self):
        response = self.client.post('/course/', {"number": "MATH231", "credit": "a"}, follow=True)
        self.assertEqual("The course credit can't use alphabets.", response.context["message"])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course by typing nothing on course name
    # Then: The system does not create course.
    # And: The system displays the course name can't be empty.
    def test_noCourseName(self):
        response = self.client.post('/course/', {"number": "", "credit": "a"}, follow=True)
        self.assertEqual("The course name can't be empty.", response.context["message"])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course by typing nothing on course name
    # Then: The system does not create course.
    # And: The system displays the course name can't be empty.
    def test_noCourseCredit(self):
        response = self.client.post('/course/', {"number": "", "credit": "a"}, follow=True)
        self.assertEqual("The course credit can't be empty.", response.context["message"])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course without typing anything.
    # Then: The system does not create course.
    # And: The system displays the course name can't be empty,
    # because the name is the section needed to be filled up first.
    def test_noCourseInformation(self):
        response = self.client.post('/course/', {"number": "", "credit": ""}, follow=True)
        self.assertEqual("The course name can't be empty.", response.context["message"])


class test_Duplicate(TestCase):
    def setUp(self):
        self.client = Client()
        user = User(name="admin", password="password")
        user.save()

        Course(number="337", credit="4").save()

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make exist.
    # When: The admin creates the new course.
    # Then: The system does not create course.
    # And: The system displays there is already course exist.
    def test_noCourseCredit(self):
        response = self.client.post('/course/', {"number": "337", "credit": "3"}, follow=True)
        self.assertEqual("The course already exist", response.context["message"])