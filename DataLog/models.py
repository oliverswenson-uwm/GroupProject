from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=100)  # staff name, i.e, John Smith
    email = models.EmailField(max_length=75)  # email fo the staff, i.e., johnsmith@uwm.edu
    username = models.CharField(max_length=100)  # user name of the staff for login, should be unique, i.e., john123
    password = models.CharField(max_length=25)  # password of the staff for login
    phoneNum = models.IntegerField()  # phone number of the staff, i.e., 4141234567
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

    # description:
    # preconditions:
    # post conditions:
    # side effects:
    def getContactInfo(self, staff):
        q = None
        staffType = ['admin', 'prof', 'ta']
        if type(staff) is None:
            return None

        if staff not in staffType:
            return q
        else:
            if staff == 'admin':
                q = Admin.objects.values('name', 'email')
            elif staff == 'prof':
                q = Professor.objects.values('name', 'email')
            elif staff == 'ta':
                q = TA.objects.values('name', 'email')

            return q

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
        # checking fields for validity/blanks
        try:
            phNumber = int(phNumber)
        except:
            return None

        if phNumber > 9999999999:
            return None
        if fullName == "" or fullName[0] == " ":
            return None
        elif email == "" or email[0] == " ":
            return None
        elif username == "" or username[0] == " ":
            return None
        elif password == "" or password[0] == " ":
            return None
        elif mailAdrs == "" or mailAdrs[0] == " ":
            return None
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
        # checking fields for validity/blanks
        try:
            phNumber = int(phNumber)
        except:
            return None

        if phNumber > 9999999999:
            return None
        if fullName == "" or fullName[0] == " ":
            return None
        elif email == "" or email[0] == " ":
            return None
        elif username == "" or username[0] == " ":
            return None
        elif password == "" or password[0] == " ":
            return None
        elif mailAdrs == "" or mailAdrs[0] == " ":
            return None
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
        # checking fields for validity/blanks
        try:
            phNumber = int(phNumber)
        except:
            return None

        if phNumber > 9999999999:
            return None
        if fullName == "" or fullName[0] == " ":
            return None
        elif email == "" or email[0] == " ":
            return None
        elif username == "" or username[0] == " ":
            return None
        elif password == "" or password[0] == " ":
            return None
        elif mailAdrs == "" or mailAdrs[0] == " ":
            return None
        ta = TA(name=fullName, email=email, username=username, password=password,
                phoneNum=phNumber, mailAddress=mailAdrs)
        ta.save()
        print(ta)
        return ta

    # description: this function would create the new course
    # preconditions: name, section credits of the course should not be empty. If one of them or all of them is empty the
    # function would return None.
    # post conditions: the new course would be created
    # side effects: Course table will have this new course in it
    def createCourse(self, nm, sec, cre, pre, des):
        if nm == "" or nm[0] == "":
            return None
        if sec == "" or sec[0] == "":
            return None
        if cre == "" or cre[0] == "":
            return None
        if not (cre.isdecimal()):
            return None
        else:
            co = Course(name=nm, section=sec, credits=cre, prereqs=pre, description=des)
            co.save()
            return co

    # description: this function will allow the creation of new Lab
    # preconditions: name should be similar to course that the lab will assign to
    # post conditions: the new lab for course will get created
    # side effects: Lab table will have this new lab in it
    def createLab(self, name, section):
        lab = None
        if not name or not section:
            return lab

        try:
            section = int(section)
        except:
            return lab

        # cheery pick bad case before creating a lab
        if type(name) is int:
            return lab
        elif name == "":
            return lab
        elif name[0] == " ":
            return lab
        elif type(name[0]) is int:
            return lab
        elif name[0] in [' @_!#$%^&*()<>?/\|}{~: ']:
            return lab
        elif section > 99999:
            return lab
        elif section < 1:
            return lab

        courseExist = Course.objects.filter(name=name)
        courseSimToLab = Course.objects.filter(name=name, section=section)
        labExist = Lab.objects.filter(name=name, section=section)
        if not courseExist:
            return lab
        elif courseSimToLab:
            return lab
        elif labExist:
            return lab

        lab = Lab(name=name, section=section)
        lab.save()
        labtocourse = None
        for e in courseExist:  # will only run once just needed to pull value out of queryset
            labtocourse = LabToCourse(lab=lab, course=e)
        labtocourse.save()
        return lab

    # description:
    # preconditions:
    # post conditions:
    # side effects:
    def assignStaff(self, user, assignment):
        pass

    # prof username and course name
    def assignProf(self, username, course, section):
        assignment = None
        # converting username to Staff Type
        userObj = Admin.getUser(self, username)
        # converting course to object
        if course is None:
            return None
        try:
            courseObj = Course.objects.get(name=course, section=section)
        except:
            return None

        print(len(ProfessorToCourse.objects.filter(course=courseObj)))
        if userObj is None:
            return None
        elif courseObj is None:
            return None
        elif 0 != len(ProfessorToCourse.objects.filter(course=courseObj)):
            return None
        assignment = ProfessorToCourse.objects.create(professor=userObj, course=courseObj)
        assignment.save()
        return assignment

    # admin can assign TAs to courses
    def assignTAToCourse(self, username, course, section):
        try:
            taObj = TA.objects.get(username=username)
        except:
            return None
        try:
            courseObj = Course.objects.get(name=course, section=section)
        except:
            return None
        if 0 != len(TAToCourse.objects.filter(ta=taObj, course=courseObj)):
            return None
        assignment = TAToCourse.objects.create(ta=taObj, course=courseObj)
        assignment.save()
        return assignment

    # removed accFlag it caused a crash, got account type from self.class
    # thank you for fixing the crash, i was planning on fixing it during lab today
    def EditAcc(self, fullName, email, username, password, phNumber, mailAdrs):
        accFlag = self.__class__
        if accFlag != "TA" or "Professor" or "Admin":
            print("You need a valid account flag. Try TA, Professor, or Admin.")

        elif accFlag == "TA":
            targ = TA(name=fullName, email=email, username=username, password=password, phoneNum=phNumber,
                      mailAddress=mailAdrs)

        elif accFlag == "Professor":
            targ = Professor(name=fullName, email=email, username=username, password=password, phoneNum=phNumber,
                             mailAddress=mailAdrs)

        elif accFlag == "Admin":
            targ = Admin(name=fullName, email=email, username=username, password=password, phoneNum=phNumber,
                         mailAddress=mailAdrs)

        targ.save()
        return targ

    def archiveAccount(self, account):
        if account is None:
            return None

        # create an archive of this account
        ArchivedUser.createArchive(self, username=account.username, name=account.name, password=account.password,
                                   phoneNum=account.phoneNum, email=account.email, mailAddress=account.mailAddress)

        # then delete this user
        staff = account.__class__
        staff.objects.get(username=account.username).delete()
        return account

    # description: Takes an account and alters the variables based on the inputs in the call
    # preconditions: User needs to have an account (a username)
    # post conditions: A user's phNumber and/or mailAdrs will be changed
    # side effects: Alters those variables in the database
    def EditContact(self, username, phNumber, mailAdrs):
        con = Admin.getUser(self, username)
        if con.phoneNum != phNumber:
            con.phoneNum = phNumber

        elif con.mailAdrs != mailAdrs:
            con.mailAdrs = mailAdrs

        con.save()
        print(con)
        return con


class Professor(Staff, models.Model):

    # description: this function assign Ta to Lab
    # preconditions: variable ta which is at the parameter is the account of ta and the variable of Lab which is at the
    # parameter is the model of lab. The account of ta and model of lab should be exist, if both of them or one of them
    # does not exist(=None), the function will return None.
    # post conditions: The ta and lab would be deleted on the database of theirs and they would updated to the database
    # of TaToLab
    # side effects: The ta and lab would be in database of TaToLab
    def assignTA(self, username, lab_name, lab_section):
        # converting username to Staff Type
        try:
            taObj = TA.objects.get(username=username)
        except:
            return None

        # converting course to object
        try:
            labObj = Lab.objects.get(name=lab_name, section=lab_section)
        except:
            return None

        if 0 != len(TAToLab.objects.filter(lab=labObj)):
            return None

        if len(Lab.objects.filter(section=lab_section)) == 0:  # check if lab exists
            return None
        if len(TA.objects.filter(username=username)) == 0:  # check if TA exists
            return None

        assignment = TAToLab.objects.create(ta=taObj, lab=labObj)
        assignment.save()
        return assignment

    def viewAssignments(self):
        assignments = []


        proftocourseobj = ProfessorToCourse.objects.filter(professor=self)

        #ITERATE THROUGH COURSES
        for c in proftocourseobj:

            i = ProfessorToCourse.getCourse(self, c)#get course
            labs = []  # reset labs because new course
            coursetolabobj = LabToCourse.objects.filter(course=i)
            if len(coursetolabobj) == 0:
                assignments.append((i, "no lab", "no TA"))
                continue

            for k in coursetolabobj:#ITERATE THROUGH ALL LABS OF GIVEN COURSE

                j = LabToCourse.getLab(self, k)
                labtotaobj = TAToLab.objects.filter(lab=j)
                if len(labtotaobj) == 0:
                    assignments.append((str(i), str(j), "no TA"))#add assignment if no TA
                    continue

                for t in labtotaobj:#ITERATE THROUGH ALL TAS IN GIVEN LABS
                    a = TAToLab.getTa(t)
                    assignments.append((str(i), str(j), str(a)))#add full assignment with course(i), lab(), ta(t)

            # TO DO: for TA in labs and make assignment class with attributes so can return list of assignment objects
        return assignments

    # description: Takes an account and alters the variables based on the inputs in the call
    # preconditions: User needs to have an account (a username)
    # post conditions: A user's phNumber and/or mailAdrs will be changed
    # side effects: Alters those variables in the database
    def EditContact(self, username, phNumber, mailAdrs):
        con = Admin.getUser(self, username)
        if con is None:
            return None

        if con.phoneNum != phNumber:
            con.phoneNum = phNumber

        elif con.mailAdrs != mailAdrs:
            con.mailAdrs = mailAdrs

        con.save()
        print(con)
        return con


class TA(Staff, models.Model):

    def viewAssignments(self):
        tatolabs = TAToLab.objects.filter(ta=self)
        if 0 == len(tatolabs):
            return []
        assignments = []
        for i in tatolabs:
            lab = i.lab
            course = LabToCourse.objects.get(lab=lab).course
            assignments.append(({"name": lab.name, "section": lab.section},
                                {"name": course.name, "section": course.section}))
        return assignments

    # description: Takes an account and alters the variables based on the inputs in the call
    # preconditions: User needs to have an account (a username)
    # post conditions: A user's phNumber and/or mailAdrs will be changed
    # side effects: Alters those variables in the database
    def EditContact(self, username, phNumber, mailAdrs):
        con = Admin.getUser(self, username)
        if con.phoneNum != phNumber:
            con.phoneNum = phNumber

        elif con.mailAdrs != mailAdrs:
            con.mailAdrs = mailAdrs

        con.save()
        print(con)
        return con

class Course(models.Model):
    name = models.CharField(max_length=100)  # name of the course, i.e., SC361
    section = models.IntegerField()  # section of this course i.e., 401
    credits = models.IntegerField()  # number of credits for this course i.e., 3
    prereqs = models.CharField(max_length=100)  # prereqs that this course required
    description = models.CharField(max_length=255)  # quick summary of the course

    # description: this function will look the Course database and will return the course,
    #   if not exists, returns None
    # preconditions: courseName and sectionNumber can not be None
    # post conditions: returns specified course
    # side effects: none
    def getCourse(self, courseName, sectionNumber):
        queryList = [Course.objects.filter(name=courseName).filter(section=sectionNumber)]
        course = None
        for query in queryList:
            if len(query) == 0:
                continue
            else:
                course = query[0]
        return course

    def __str__(self):
        return self.name + "-" + str(self.section)


class Lab(models.Model):
    # name of the lab, should be similar to course name
    # since its is assigning to a course, i.e.,  CS361
    name = models.CharField(max_length=100)
    section = models.IntegerField()  # section of lab, i.e., 802

    def __str__(self):
        return self.name + "-" + str(self.section)


class ArchivedUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=25)
    phoneNum = models.IntegerField()
    mailAddress = models.CharField(max_length=100)

    def createArchive(self, name, email, username, password, phoneNum, mailAddress):
        temp = ArchivedUser(name=name, email=email, username=username, password=password, phoneNum=phoneNum,
                            mailAddress=mailAddress)
        temp.save()
        return temp


class LabToCourse(models.Model):
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def getLab(self, coursetolabobj):
        return coursetolabobj.lab

    def getCourse(self, coursetolabobj):
        return coursetolabobj.course
    def __str__(self):
        return "Lab " + self.lab.__str__() + " is assigned to course " + self.course.__str__()


class ProfessorToCourse(models.Model):
    # This table is cascaded, mean if any of those field get deleted the whole will get deleted from this table
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def getCourse(self, e):
        return e.course

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

    # description: this function would return the ta of TAToLab
    # preconditions: Ta should not be None
    # post conditions: return ta
    # side effects: None
    def getTa(self):
        return self.ta

    # description: this function would return the lab of TAToLab
    # preconditions: Lab should not be None
    # post conditions: return lab
    # side effects: None
    def getLab(self):
        return self.lab

    def __str__(self):
        return "TA " + self.ta.__str__() + " is assigned to lab " + self.lab.__str__()
