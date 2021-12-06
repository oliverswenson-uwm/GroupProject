from django.test import TestCase

from django.test import Client

from DataLog.models import *


# Writing test as admin as user which have their name as admin.
# Writing test Course as course database.

class test_noDuplicate(TestCase):
    def setUp(self):
        self.client = Client()
        Course(name="COMPSCI361", section="401", credits="3", prereqs="COMPSCI251",
               description="Introduction to software engineering").save()

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new courses by entering the course number, credits,
    # prerequisites, and a course description.
    # Then: The course is created at page.

    def test_defualt(self):
        response = self.client.post('/createcourse/', {"name": "MATH231", "section": "401", "credits": "3",
                                                       "prereqs": "Math101", "description": "Algebra"}, follow=True)
        self.assertEqual("MATH231", response.context["name"])
        self.assertEqual("3", response.context["credits"])
        self.assertEqual("401", response.context["section"])
        self.assertEqual("Math101", response.context["prereqs"])
        self.assertEqual("Algebra", response.context["description"])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course by using alphabets on credits.
    # Then: The system does not create course.
    # And: The system displays the course credits can't be using alphabets.
    def test_invalidCourseCredit(self):
        response = self.client.post('/createcourse/', {"name": "MATH231", "section": "401", "credits": "asdf",
                                                       "prereqs": "Math101", "description": "Algebra"}, follow=True)
        self.assertEqual("Credits should be number between 0 and 9", response.context['msg'])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course by typing nothing on course name
    # Then: The system does not create course.
    # And: The system displays the course name can't be empty.
    def test_noCourseName(self):
        response = self.client.post('/createcourse/', {"name": "", "section": "401", "credits": "3"}, follow=True)
        self.assertEqual("Course name cannot be empty", response.context['msg'])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course by typing nothing on course name
    # Then: The system does not create course.
    # And: The system displays the course name can't be empty.
    def test_noCourseSection(self):
        response = self.client.post('/createcourse/', {"name": "Math231", "section": "", "credits": "3"}, follow=True)
        self.assertEqual("Course section cannot be empty", response.context['msg'])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course by typing nothing on course credit
    # Then: The system does not create course.
    # And: The system displays the course credit can't be empty.
    def test_noCourseCredit(self):
        response = self.client.post('/createcourse/', {"name": "Math231", "section": "401", "credits": ""}, follow=True)
        self.assertEqual("Course credit cannot be empty", response.context['msg'])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course by typing nothing on course prerequisites
    # Then: The system create the new course.(=Because prerequisites are not essential)
    def test_noCourePrereqs(self):
        response = self.client.post('/createcourse/', {"name": "MATH231", "section": "401", "credits": "3",
                                                       "prereqs": "", "description": "Algebra"}, follow=True)
        self.assertEqual("MATH231", response.context["name"])
        self.assertEqual("3", response.context["credits"])
        self.assertEqual("401", response.context["section"])
        self.assertEqual("", response.context["prereqs"])
        self.assertEqual("Algebra", response.context["description"])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course by typing nothing on course description
    # Then: The system create the new course.(=Because descriptions are not essential)
    def test_noCoureDescription(self):
        response = self.client.post('/createcourse/', {"name": "MATH231", "section": "401", "credits": "3",
                                                       "prereqs": "MATH101", "description": ""}, follow=True)
        self.assertEqual("MATH231", response.context["name"])
        self.assertEqual("3", response.context["credits"])
        self.assertEqual("401", response.context["section"])
        self.assertEqual("MATH101", response.context["prereqs"])
        self.assertEqual("", response.context["description"])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make does not exist.
    # (=There is no course in database that have same course number which admin just typed.)
    # When: The admin creates the new course without typing anything.
    # Then: The system does not create course.
    # And: The system displays the course name can't be empty,
    # because the course name is at the front, the course name should be filled up first.
    def test_noCourseInformation(self):
        response = self.client.post('/createcourse/', {"name": "", "section": "", "credits": "",
                                                       "prereqs": "", "description": ""}, follow=True)
        self.assertEqual("Course name cannot be empty", response.context['msg'])


class test_Duplicate(TestCase):
    def setUp(self):
        self.client = Client()
        Course(name="COMPSCI361", section="401", credits="3", prereqs="COMPSCI251",
               description="Introduction to software engineering").save()

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make exist.
    # When: The admin creates the new course.
    # Then: The system does not create course.
    # And: The system displays there is already course exist.
    def test_DuplicaeName(self):
        response = self.client.post('/createcourse/', {"name": "COMPSCI361",
                                                       "section": "401", "credits": "3", "prereqs": "COMPSCI251",
                                                       "description": "Introduction to software engineering"},
                                    follow=True)
        self.assertEqual("The course already exist", response.context['msg'])

    # As a system admin, I want to create a new course, so that I could add new courses on the page.
    # Given: The course that admin is trying to make exist(=Only the name is same).
    # When: The admin creates the new course.
    # Then: The system does not create course.
    # And: The system displays there is already course exist.
    def test_OnlyDuplicateName(self):
        # Only section different
        response = self.client.post('/createcourse/', {"name": "COMPSCI361",
                                                       "section": "301", "credits": "3", "prereqs": "COMPSCI251",
                                                       "description": "Introduction to software engineering"}
                                    , follow=True)
        self.assertEqual("The course already exist", response.context['msg'])

        # Only credit different
        response = self.client.post('/createcourse/', {"name": "COMPSCI361",
                                                       "section": "401", "credits": "4", "prereqs": "COMPSCI251",
                                                       "description": "Introduction to software engineering"},
                                    follow=True)
        self.assertEqual("The course already exist", response.context['msg'])

        # Only prereqs different
        response = self.client.post('/createcourse/', {"name": "COMPSCI361",
                                                       "section": "401", "credits": "4", "prereqs": "AA",
                                                       "description": "Introduction to software engineering"},
                                    follow=True)
        self.assertEqual("The course already exist", response.context['msg'])

        # Only descrption different
        response = self.client.post('/createcourse/', {"name": "COMPSCI361",
                                                       "section": "401", "credits": "4", "prereqs": "COMPSCI251",
                                                       "description": "AA"}, follow=True)
        self.assertEqual("The course already exist", response.context['msg'])

        # Only Name is equal, and everything is different.

        response = self.client.post('/createcourse/', {"name": "COMPSCI361",
                                                       "section": "101", "credits": "7", "prereqs": "ABC",
                                                       "description": "AA"}, follow=True)
        self.assertEqual("The course already exist", response.context['msg'])
