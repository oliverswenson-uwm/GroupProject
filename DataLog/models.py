from django.db import models


class Staff(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=25)
    phoneNum = models.IntegerField()
    mailAddress = models.CharField(max_length=100)

    # any user can change there personal information
    # def setFirstName(self, name):
    #     pass
    #
    # def setLastName(self, name):
    #     pass
    #
    # def setEmail(self, email):
    #     pass

    # This function will return first and last name and email of all users
    def getPublicInfo(self):
        pass

    def __str__(self):
        return self.firstName + " " + self.lastName

    class Meta:
        abstract = True


class Admin(Staff, models.Model):

    def createAccount(self):
        pass

    def createCourse(self):
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
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Lab(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


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