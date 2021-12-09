from DataLog.models import Staff, Professor, Assignment, Admin
from django.test import TestCase

#testcases written such that professor creates assignment calling professor.createAssignment
#assignments are retrieved by calling professor.viewCourseAssignments()
#design can be changed as see fit


class testGetAssignmentsGood(TestCase):

    def testGetAssignmentOne(self):
        prof1 = Admin.createProf(self, fullName="TestprofOne", email="proftesting1@gmail.com", username="testprofoneuser",
                         password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")

        #professor creates assignment
        prof1.createAssignment(name = "assignmentOne", dueDate = "12/20/21", course = "cs361")
        #professor queries to see their assignments for course
        assignments = prof1.viewCourseAssignments(course = "cs361")
        #make sure assignment returns
        self.assertEqual(assignments, "assignmentOne")

    def testGetAssignmentTwo(self):
        prof2 = Admin.createProf(self, fullName="Testproftwo", email="proftesting2@gmail.com", username="testproftwouser",
                         password="profpasstwo", phNumber=2223332222, mailAdrs="2 Professor St.")
        #professor creates assignment
        prof2.createAssignment(name = "assignmentTwo", dueDate = "12/22/21", course = "cs337")
        #professor queries to see their assignments for course
        assignments = prof2.viewCourseAssignments(course = "cs337")
        #make sure assignment returns
        self.assertEqual(assignments, "cs337")


class testGetAssignmentsFail(TestCase):

    def returnNone(self):
        prof2 = Admin.createProf(self, fullName="Testproftwo", email="proftesting2@gmail.com",username="testproftwouser",
                                 password="profpasstwo", phNumber=2223332222, mailAdrs="2 Professor St.")
        assignments = prof2.viewCourseAssignments(course="")
        self.assertEqual(assignments, None)
