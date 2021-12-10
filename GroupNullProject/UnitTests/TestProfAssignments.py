from DataLog.models import Staff, Professor, Admin, Lab, LabToCourse, ProfessorToCourse, TAToLab, TAToCourse
from django.test import TestCase


class testGetAssignmentsGood(TestCase):
    def setUp(self):
        # create professor
        self.prof1 = Admin.createProf(self, fullName="TestprofOne", email="proftesting1@gmail.com",
                                           username="testprofoneuser",
                                           password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        # create TA
        Admin.createTA(self, fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                       password="testpassoneTA", phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        # create courses
        Admin.createCourse(self, nm="compsci361", sec="401", cre="3", pre="compsci251", des="")
        Admin.createCourse(self, nm="compsci351", sec="122", cre="3", pre="compsci251", des="")
        # create Labs
        lab1 = Admin.createLab(name="compsci361", section=123)
        lab2 = Admin.createLab(name="compsci351", section=333)
        # assign prof to courses
        Admin.assignProf(prof="testprofoneuser", course="compsci361")
        Admin.assignProf(prof="testprofoneuser", course="compsci351")
        #assign TA to labs
        Admin.assignTA(ta = "TestTAone", lab = lab1)
        Admin.assignTA(ta="TestTAone", lab=lab2)
    def testGetAssignmentOne(self):
        self.assertEqual(self.prof1.viewAssignments().TA,"testTAone")
        self.assertEqual(self.prof1.viewAssignments().course, "compsci361")
        self.assertEqual(self.prof1.viewAssignments().section, 123)

    def testGetAssignmentTwo(self):
        self.assertEqual(self.prof1.viewAssignments().TA,"testTAone")
        self.assertEqual(self.prof1.viewAssignments().course, "compsci351")
        self.assertEqual(self.prof1.viewAssignments().section, 333)

class testGetAssignmentsFail(TestCase):
    def setUp(self):
        # create professor
        self.prof1 = Admin.createProf(self, fullName="TestprofOne", email="proftesting1@gmail.com",
                                           username="testprofoneuser",
                                           password="profpassone", phNumber=1231231233, mailAdrs="1 Professor St.")
        self.noAssignmentProf = Admin.createProf(self, fullName="noAssignments", email="assignmentless@gmail.com",
                                      username="testprofnoAssign", password="password", phNumber=2222333366, mailAdrs="1 Assignment St.")
        self.prof2 = None
        # create TA
        Admin.createTA(self, fullName="TestTAone", email="taOnGmail1@gmail.com", username="testTAone",
                       password="testpassoneTA", phNumber=3334441111, mailAdrs="2 TeachingAssistant Circle")
        # create courses
        Admin.createCourse(self, nm="compsci361", sec="401", cre="3", pre="compsci251", des="")
        Admin.createCourse(self, nm="compsci351", sec="122", cre="3", pre="compsci251", des="")
        # create Labs
        lab1 = Admin.createLab(name="compsci361", section=123)
        lab2 = Admin.createLab(name="compsci351", section=333)
        # assign prof to courses
        Admin.assignProf(prof="testprofoneuser", course="compsci361")
        Admin.assignProf(prof="testprofoneuser", course="compsci351")
        #assign TA to labs
        Admin.assignTA(ta = "TestTAone", lab = lab1)
        Admin.assignTA(ta="TestTAone", lab=lab2)

    def testProfNotExist(self):
        self.assertEqual(self.prof2.viewAssignments(), None)#prof that doesn't exist

    def testNoAssignments(self):
        self.assertEqual(self.noAssignmentProf().viewAssignments(), None)
