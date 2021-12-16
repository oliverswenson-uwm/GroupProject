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

        # create Labs
        lab1 = Admin.createLab(self, name="compsci361", section=123)
        lab2 = Admin.createLab(self, name="compsci351", section=333)

        # assign prof to courses
        Admin.assignProf(self, prof=self.prof1, course=self.cs361)
        Admin.assignProf(self, prof=self.prof1, course=self.cs351)

        #assign TA to labs
        #TODO: use professor's function instead to assign to lab?
        Professor.add_taLab(ta=testTaone, lab=lab1)
        Professor.add_taLab(ta=testTaone, lab=lab2)

    def testGetAssignmentOne(self):
        self.assertEqual(self.prof1.viewAssignments(),"[compsci361 : Lab08 : TestTAone]")

    def testGetAssignmentTwo(self):
        self.assertEqual(self.prof1.viewAssignments(),"[compsci351 : Lab07 : TestTAone]")

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
        lab1 = Admin.createLab(self, name="compsci361", section=123)
        lab2 = Admin.createLab(self, name="compsci351", section=333)
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
