from django.test import TestCase
from DataLog.models import *


class TestCreateCourse(TestCase):

    def test_create_well_one(self):
        Admin.createCourse(nm="compsci361", sec="401", cre="3", pre="compsci251", des="")
        temp = Course.getCourse("compsci361", "401")
        self.assertEqual(temp.name, "compsci361")
        self.assertEqual(temp.section, 401)
        self.assertEqual(temp.credits, 3)

    def test_create_well_two(self):
        Admin.createCourse(nm="compsci351", sec="301", cre="3", pre="", des="Intro")
        temp = Course.getCourse("compsci351", "301")
        self.assertEqual(temp.name, "compsci351")
        self.assertEqual(temp.section, 301)

    def test_create_well_third(self):
        Admin.createCourse(nm="compsci351", sec="301", cre="3", pre="compsci251", des="Intro")
        temp = Course.getCourse("compsci351", "301")
        self.assertEqual(temp.name, "compsci351")
        self.assertEqual(temp.section, 301)

    def test_empty_Name(self):
        Admin.createCourse(nm="", sec="301", cre="3", pre="", des="")
        temp = Course.getCourse("", "301")
        self.assertEqual(temp, None)

    def test_empty_Two(self):
        Admin.createCourse(nm="", sec="401", cre="4", pre="", des="")
        temp = Course.getCourse("", "401")
        self.assertEqual(temp, None)

    def test_empty_Sec_One(self):
        Admin.createCourse(nm="compsci361", sec="", cre="3", pre="compsci251", des="")
        temp = Course.getCourse("compsci361", "401")
        self.assertEqual(temp, None)

    def test_empty_Sec_One(self):
        Admin.createCourse(nm="compsci351", sec="", cre="3", pre="compsci251", des="")
        temp = Course.getCourse("compsci351", "301")
        self.assertEqual(temp, None)

    def test_empty_Cre_One(self):
        Admin.createCourse(nm="compsci361", sec="401", cre="", pre="compsci251", des="")
        temp = Course.getCourse("compsci361", "401")
        self.assertEqual(temp, None)

    def test_empty_Cre_Two(self):
        Admin.createCourse(nm="compsci351", sec="401", cre="", pre="compsci251", des="")
        temp = Course.getCourse("compsci351", "401")
        self.assertEqual(temp, None)

    def test_Bad_Cre_One(self):
        Admin.createCourse(nm="compsci351", sec="401", cre="asdf", pre="compsci251", des="")
        temp = Course.getCourse("compsci351", "401")
        self.assertEqual(temp, None)

    def test_Bad_Cre_One(self):
        Admin.createCourse(nm="compsci361", sec="301", cre="1sdf", pre="compsci251", des="")
        temp = Course.getCourse("compsci361", "301")
        self.assertEqual(temp, None)

