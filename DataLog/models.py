from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=100)  # staff name, i.e, John Smith
    email = models.EmailField(max_length=75)  # email fo the staff, i.e., johnsmith@uwm.edu
    username = models.CharField(max_length=100)  # user name of the staff for login, should be unique, i.e., john123
    password = models.CharField(max_length=25)  # password of the staff for login
    phoneNum = models.IntegerField()  # phone number of the staff, i.e., 4141234567
    mailAddress = models.CharField(max_length=100)  # main address of staff i.e., 1234 N 12st
    # any user can change there personal information
    # def setFirstName(self, name):
    #     pass
    #
    # def setLastName(self, name):
    #     pass
    #
    # def setEmail(self, email):
    #     pass

    def getUser(self, username):
        queryList = []
        queryList.append(Admin.objects.filter(username=username))
        queryList.append(Professor.objects.filter(username=username))
        queryList.append(TA.objects.filter(username=username))
        # a = queryList[0]
        print(queryList)
        user = None
        for query in queryList:
            if len(query) == 0:
                continue
            else:
                user = query[0]
        return user

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Admin(Staff, models.Model):
    def createAdmin(self, fullName, email, username, password, phNumber, mailAdrs):
        admin = Admin(name=fullName, email=email, username=username, password=password, phoneNum=phNumber, mailAddress=mailAdrs)
        admin.save()
        print(admin)
        return admin

    def createProf(self, fullName, email, username, password, phNumber, mailAdrs):
        prof = Professor(name=fullName, email=email, username=username, password=password, phoneNum=phNumber, mailAddress=mailAdrs)
        prof.save()
        print(prof)
        return prof

    def createTA(self, fullName, email, username, password, phNumber, mailAdrs):
        ta = TA(name=fullName, email=email, username=username, password=password, phoneNum=phNumber, mailAddress=mailAdrs)
        ta.save()
        print(ta)
        return ta

    def createCourse(self):
        pass

    def assignStaff(self):
        pass


class Professor(Staff, models.Model):

    def assignTA(self, ta, lab):
        pass

    def viewCourseAssignments(self):
        pass


class TA(Staff, models.Model):

    def viewAssignments(self):
        pass


class Course(models.Model):
    name = models.CharField(max_length=100)  # name of the course, i.e., SC361
    section = models.IntegerField()  # section of this course i.e., 401
    credits = models.IntegerField()  # number of credits for this course i.e., 3
    prereqs = models.CharField(max_length=100)  # prereqs that this course required
    description = models.CharField(max_length=255)  # quick summary of the course

    def __str__(self):
        return self.name + "-" + str(self.section)


class Lab(models.Model):
    # name of the lab, should be similar to course name
    # since its is assigning to a course, i.e.,  CS361
    name = models.CharField(max_length=100)
    section = models.IntegerField()  # section of lab, i.e., 802

    def __str__(self):
        return self.name + "-" + self.section


class LabToCourse(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "Lab " + self.ta.__str__() + " is assigned to course " + self.course.__str__()


class ProfessorToCourse(models.Model):
    # This table is cascaded, mean if any of those field get deleted the whole will get deleted from this table
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "Professor " + self.professor.__str__() + " is assigned to course " + self.course.__str__()


class TAToCourse(models.Model):
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "TA " + self.ta.__str__() + " is assigned to course " + self.course.__str__()


class TAToLab(models.Model):
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

    def __str__(self):
        return "TA " + self.ta.__str__() + " is assigned to lab " + self.lab.__str__()
