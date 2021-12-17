from DataLog.models import Staff, Professor, Admin, Lab, LabToCourse, ProfessorToCourse, TAToLab, TAToCourse
from django.test import TestCase


class testGetAssignmentsGood(TestCase):
    def setUp(self):
        # create professor
        self.prof1 = Admin.createProf(self, fullName="TestprofOne", email="proftesting1@gmail.com",
                                           username="testprofoneuser",
                                           password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        # create TA
        testTaone = Admin.createTA(self, fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                       password="testpassoneTA", phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        # create courses
        self.cs361 = Admin.createCourse(self, nm="compsci361", sec="401", cre="3", pre="compsci251", des="")
        self.cs351 = Admin.createCourse(self, nm="compsci351", sec="122", cre="3", pre="compsci251", des="")
        self.cs777 = Admin.createCourse(self, nm="compsci777", sec="444", cre="3", pre="compsci251", des="")

        # create Labs
        lab1 = Admin.createLab(self, name="compsci361", section=123)
        lab2 = Admin.createLab(self, name="compsci351", section=333)
        lab3 = Admin.createLab(self, name="compsci777", section=555)

        # assign prof to courses
        Admin.assignProf(self, username=self.prof1.username, course=self.cs361.name, section = self.cs361.section)
        Admin.assignProf(self, username=self.prof1.username, course=self.cs351.name, section = self.cs351.section)
        Admin.assignProf(self, username=self.prof1.username, course=self.cs777.name, section = self.cs777.section)

        #assign TA to labs
        #TODO: use professor's function instead to assign to lab?
        Professor.add_taLab(self,ta=testTaone, lab=lab1)
        Professor.add_taLab(self,ta=testTaone, lab=lab2)

    def testGetAssignmentOne(self):
        self.assertTrue(self.prof1.viewAssignments().__contains__(('compsci361-401', 'compsci361-123', 'TestTAone')))
    def testGetAssignmentTwo(self):
        self.assertTrue(self.prof1.viewAssignments().__contains__(('compsci351-122', 'compsci351-333', 'TestTAone')))
    def testNoTA(self):
        self.assertTrue(self.prof1.viewAssignments().__contains__(('compsci777-444', 'compsci777-555', 'no TA')))

class testGetAssignmentsFail(TestCase):

    def testNoAssignments(self):
        self.noAssignmentProf = Admin.createProf(self, fullName="NoAssignment", email="proftesting1@gmail.com",
                                            username="Noassignmentprof",
                                            password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        self.assertEqual(len(self.noAssignmentProf.viewAssignments()),0)#prof that doesn't exist

