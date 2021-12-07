from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=100)  # staff name, i.e, John Smith
    email = models.EmailField(max_length=75)  # email fo the staff, i.e., johnsmith@uwm.edu
    username = models.CharField(max_length=100)  # user name of the staff for login, should be unique, i.e., john123
    password = models.CharField(max_length=25)  # password of the staff for login
    phoneNum = models.IntegerField()  # phone number of the staff, i.e., 4141234567 #TODO: max length 10?
    mailAddress = models.CharField(max_length=100)  # main address of staff i.e., 1234 N 12st

    # description: this function will look the Staff database and will return the user,
    #   if not exists, returns None
    # preconditions: username can not be None type
    # post conditions: user from the table if exists, will get returned
    # side effects: none
    def getUser(self, username):
        queryList = [Admin.objects.filter(username=username), Professor.objects.filter(username=username),
                     TA.objects.filter(username=username)]
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
    # description: this function will create a admin in Admin database
    # preconditions: all fields should be valid and not None type, username should be unique
    # post conditions: the admin will get created in Admin table
    # side effects: Admin table will get modified
    def createAdmin(self, fullName, email, username, password, phNumber, mailAdrs):
        admin = Admin(name=fullName, email=email, username=username, password=password,
                      phoneNum=phNumber, mailAddress=mailAdrs)
        admin.save()
        print(admin)
        return admin

    # description: this function will create a professor in Professor database
    # preconditions: all fields should be valid and not None type, username should be unique
    # post conditions: the professor will get created in Professor table
    # side effects: Professor table will get modified
    def createProf(self, fullName, email, username, password, phNumber, mailAdrs):
        prof = Professor(name=fullName, email=email, username=username, password=password,
                         phoneNum=phNumber, mailAddress=mailAdrs)
        prof.save()
        print(prof)
        return prof

    # description: this function will create a ta in TA database
    # preconditions: all fields should be valid and not None type, username should be unique
    # post conditions: the ta will get created in TA table
    # side effects: TA table will get modified
    def createTA(self, fullName, email, username, password, phNumber, mailAdrs):
        ta = TA(name=fullName, email=email, username=username, password=password,
                phoneNum=phNumber, mailAddress=mailAdrs)
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

    # description: this function will look the Course database and will return the course,
    #   if not exists, returns None
    # preconditions: courseName and sectionNumber can not be None
    # post conditions: returns specified course
    # side effects: none
    def getCourse(self, courseName, sectionNumber):
        queryList = [Course.objects.filter(name=courseName).filter(section=sectionNumber)]
        print(queryList)
        course = None
        for query in queryList:
            if len(query) == 0:
                continue
            else:
                course = query[0]
        return course


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
