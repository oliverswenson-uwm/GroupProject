from DataLog.models import Staff, Professor, Assignment, Admin
from django.test import TestCase

#testcases written such that professor creates assignment calling professor.createAssignment
#assignments are retrieved by calling professor.viewCourseAssignments()
#design can be changed as see fit


class testGetAssignmentsGood(TestCase):

    def testGetAssignmentOne(self):
        pass

    def testGetAssignmentTwo(self):
        pass

class testGetAssignmentsFail(TestCase):

    def testReturnNone(self):
        pass
