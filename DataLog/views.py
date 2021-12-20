from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from DataLog.models import Staff, Admin, Professor, TA, Course, Lab, LabToCourse, ProfessorToCourse, TAToCourse, TAToLab


class Login(View):
    def get(self, request):
        request.session.flush()  # log out any logged user
        return render(request, "index.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = Staff.getUser(self, username)
        if user:
            if password == user.password:
                if isinstance(user, Admin):
                    request.session['user'] = user.username
                    request.session['role'] = 'admin'
                    return redirect("/supervisor/")
                elif isinstance(user, Professor):
                    request.session['user'] = user.username
                    request.session['role'] = 'professor'
                    return redirect("/professor/")
                elif isinstance(user, TA):
                    request.session['user'] = user.username
                    request.session['role'] = 'ta'
                    return redirect("/ta/")
            else:
                request.session.flush()  # log out logged user
                messages.add_message(request, messages.INFO, 'INVALID Username OR Password')
                return render(request, "index.html", {'msg': 'INVALID Username OR Password'})
        else:  # user is None, mean invalid username or password or user does not exist
            request.session.flush()  # log out logged user
            messages.add_message(request, messages.INFO, 'INVALID Username OR Password')
            return render(request, "index.html", {'msg': 'INVALID Username OR Password'})


class AdminView(View):
    def get(self, request):
        # the following if else statement check if someone is logged in or not
        # if logged and the user is not admin
        # the person will get redirected to logging page
        if 'role' in request.session:
            role = request.session['role']
            if role != 'admin':
                return redirect('/', {'msg': 'Please logging as Admin'})
        else:
            return redirect('/', {'msg': 'Please logging as Admin'})

        return render(request, "adminpage.html")


class ProfessorView(View):
    def get(self, request):
        # the following if else statement check if someone is logged in or not
        # if logged and the user is not admin
        # the person will get redirected to logging page
        if 'role' in request.session:
            role = request.session['role']
            if role != 'professor':
                return redirect('/', {'msg': 'Please logging as Professor'})
        else:
            return redirect('/', {'msg': 'Please logging as Professor'})

        return render(request, "profpage.html")


class TaView(View):
    def get(self, request):
        # the following if else statement check if someone is logged in or not
        # if logged and the user is not admin
        # the person will get redirected to logging page
        if 'role' in request.session:
            role = request.session['role']
            if role != 'ta':
                return redirect('/', {'msg': 'Please logging as TA'})
        else:
            return redirect('/', {'msg': 'Please logging as TA'})

        labCourseQuery = TA.objects.get(username=request.session["username"]).viewAssignments(self)
        coursesQuery = []
        labsQuery = []
        for links in labCourseQuery:
            labsQuery.append(links[0])
            coursesQuery.append(links[1])

        return render(request, "tapage.html", {"coursesQuery": coursesQuery, "labsQuery": labsQuery})


class CreateUser(View):
    def get(self, request):
        # the following if else statement check if someone is logged in or not
        # if logged and the user is not admin
        # the person will get redirected to logging page
        if 'role' in request.session:
            role = request.session['role']
            if role != 'admin':
                messages.add_message(request, messages.INFO, 'Please logging as Admin')
                return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Please logging as Admin')
            return redirect('/')

        return render(request, "newacc.html")

    def post(self, request):
        fullName = request.POST['fullName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        phNumber = request.POST['phNumber']
        mailAdrs = request.POST['mailAdrs']
        accType = request.POST['accType']

        print(accType)
        user = Staff.getUser(self, username)
        if not user:  # username does not exits(new user is being created)
            newUser = None
            if accType == 'admin':
                newUser = Admin.createAdmin(self, fullName, email, username, password, phNumber, mailAdrs)
                print(newUser)
                if newUser is None:
                    return render(request, "newacc.html", {'msg': "Failed: A empty field in form"})
            elif accType == 'prof':
                newUser = Admin.createProf(self, fullName, email, username, password, phNumber, mailAdrs)
                print(newUser)
                if newUser is None:
                    return render(request, "newacc.html", {'msg': "Failed: A empty field in form"})
            elif accType == 'ta':
                newUser = Admin.createTA(self, fullName, email, username, password, phNumber, mailAdrs)
                print(newUser)
                if newUser is None:
                    return render(request, "newacc.html", {'msg': "Failed: A empty field in form"})
            return render(request, "newacc.html", {'msg': "Success: New Account has been create "})
        else:
            return render(request, "newacc.html", {'msg': "Fail: Username exist, Please Pick a new Username"})


# ASSIGNTATOCOURSE
class AssignTAToCourse(View):
    def get(self, request):
        # the following if else statement check if someone is logged in or not
        # if logged and the user is not admin
        # the person will get redirected to logging page
        if 'role' in request.session:
            role = request.session['role']
            if role != 'admin':
                messages.add_message(request, messages.INFO, 'Please logging as Admin')
                return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Please logging as Admin')
            return redirect('/')

        taQuery = TA.objects.all().values('name', 'username').distinct()
        courseQuery = Course.objects.all().values('name', 'section').distinct()

        return render(request, "assignTAToCourse.html", {"taQuery": taQuery, "courseQuery": courseQuery})

    def post(self, request):
        ta = request.POST['taSel'].split('-')  # output ['name', 'username']
        course = request.POST['courseSel'].split('-')  # output ['name', 'section']
        username = ta[1]
        courseName = course[0]
        courseSection = course[1]
        assignment = Admin.assignTAToCourse(self, username, courseName, courseSection)

        if assignment is None:
            messages.add_message(request, messages.INFO, 'Unable to add TA to Course')
            return redirect("/tatocourse/")
        messages.add_message(request, messages.INFO, 'TA assigned')
        return redirect("/tatocourse/")


# I just added the site as assignta.html. If you want to change feel free to change it.
class AssignTaToLab(View):
    def get(self, request):
        if 'role' in request.session:
            role = request.session['role']
            if role != 'professor':
                messages.add_message(request, messages.INFO, 'Please logging as professor')
                return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Please logging as professor')
            return redirect('/')

        labQuery = Lab.objects.all().values('name', 'section').distinct()
        taQuery = TA.objects.all().values('name', 'username').distinct()

        return render(request, "assignTAToLab.html", {"labQuery": labQuery, "taQuery": taQuery})

    def post(self, request):
        ta = request.POST['taSel']
        lab = request.POST['labSel'].split('-')
        username = ta.split('-')[1]
        lab_name = lab[0]
        lab_section = lab[1]
        assignment = Professor.assignTA(self, username, lab_name, lab_section)

        if assignment is None:
            messages.add_message(request, messages.INFO, 'Unable to add Ta to Lab')
            return redirect("/tatoLab/")
        messages.add_message(request, messages.INFO, 'TA assigned')
        return redirect("/tatoLab/")


# CREATECOURSE
class CreateCourse(View):
    def get(self, request):
        return render(request, "createcourse.html", {})

    def post(self, request):
        try:
            m = Course.objects.get(name=request.POST['name'], section=request.POST['section'])
            if m is not None:
                return render(request, "createcourse.html", {'msg': "The course already exist"})
        except:
            if request.POST['name'] == "":
                return render(request, "createcourse.html", {'msg': "Course name cannot be empty"})
            if request.POST['section'] == "":
                return render(request, "createcourse.html", {'msg': "Course section cannot be empty"})
            if request.POST['credits'] == "":
                return render(request, "createcourse.html", {'msg': "Course credit cannot be empty"})
            if '0' > request.POST['credits'] or request.POST['credits'] > '9':
                return render(request, "createcourse.html", {'msg': "Credits should be number between 0 and 9"})
            else:
                # Course(name=request.POST['name'], section=request.POST['section'], credits=request.POST['credits'],
                #        prereqs=request.POST['prereqs'], description=request.POST['description']).save()
                nm = request.POST['name']
                sec = request.POST['section']
                cre = request.POST['credits']
                pre = request.POST['prereqs']
                des = request.POST['description']
                Admin.createCourse(self, nm, sec, cre, pre, des)
            return render(request, "createcourse.html", {'name': request.POST['name'],
                                                         'section': request.POST['section'],
                                                         'credits': request.POST['credits'],
                                                         'prereqs': request.POST['prereqs'],
                                                         'description': request.POST['description'],
                                                         'msg': "The course has been created."})


class CreateLab(View):

    def get(self, request):
        # the following if else statement check if someone is logged in or not
        # if logged and the user is not admin
        # the person will get redirected to logging page
        if 'role' in request.session:
            role = request.session['role']
            if role != 'admin':
                messages.add_message(request, messages.INFO, 'Please logging as Admin')
                return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Please logging as Admin')
            return redirect('/')

        courseQuery = Course.objects.all().values('name').distinct()

        return render(request, "createLab.html", {"courseQuery": courseQuery})

    def post(self, request):
        labName = request.POST['labName']
        labSec = request.POST['labSec']
        print(labName, labSec)
        newLab = Admin.createLab(self, labName, labSec)
        print(newLab)
        if newLab is None:
            messages.add_message(request, messages.INFO, 'Failed to create Lab')
            return redirect("/createlab/")
        messages.add_message(request, messages.INFO, 'Lab created Successfully!')
        return redirect("/createlab/")


# view for assigning professor to the course
class AssignProf(View):
    def get(self, request):
        # the following if else statement check if someone is logged in or not
        # if logged and the user is not admin
        # the person will get redirected to logging page
        if 'role' in request.session:
            role = request.session['role']
            if role != 'admin':
                messages.add_message(request, messages.INFO, 'Please logging as Admin')
                return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Please logging as Admin')
            return redirect('/')

        profQuery = Professor.objects.all().values('name', 'username').distinct()
        courseQuery = Course.objects.all().values('name', 'section').distinct()

        return render(request, "assignprof.html", {"profQuery": profQuery, "courseQuery": courseQuery})

    def post(self, request):
        prof = request.POST['profSel'].split('-')  # output ['name', 'username']
        course = request.POST['courseSel'].split('-')  # output ['name', 'section']
        username = prof[1]
        courseName = course[0]
        courseSection = course[1]

        assignment = Admin.assignProf(self, username, courseName, courseSection)

        if assignment is None:
            messages.add_message(request, messages.INFO, 'Unable to add professor to Course')
            return redirect("/assignprof/")
        messages.add_message(request, messages.INFO, 'Professor assigned')
        return redirect("/assignprof/")


# public contact Info
class ContactInfo(View):
    def get(self, request):
        # the following if else statement check if someone is logged in or not
        # if logged and the user is not the staff of school
        # the person will get redirected to logging page
        if 'role' in request.session:
            role = request.session['role']
            print(request.session)
            return render(request, "contactInfo.html")
        else:
            messages.add_message(request, messages.INFO, 'Please logging as Staff')
            return redirect('/')

    def post(self, request):
        staff = request.POST['staff']
        contactQuery = None
        print(staff)
        if staff == "admin":
            contactQuery = Admin.getContactInfo(self, staff)
        elif staff == "prof":
            contactQuery = Professor.getContactInfo(self, staff)
        elif staff == "ta":
            contactQuery = TA.getContactInfo(self, staff)

        if contactQuery is None:
            return render(request, "contactInfo.html", {'msg': "Invalid Staff Type"})
        else:
            return render(request, "contactInfo.html", {"query": contactQuery})


# View for admin to look up data in system
class Lookup(View):
    def get(self, request):
        if 'role' in request.session:
            role = request.session['role']
            if role != 'admin':
                messages.add_message(request, messages.INFO, 'Please logging as Admin')
                return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Please logging as Admin')
            return redirect('/')

        return render(request, "dataLookup.html")

    def post(self, request):
        lookup = request.POST['lookup']
        lookupType = None

        if lookup == "admin":
            query = Admin.objects.all()
            lookupType = "staff"
        elif lookup == "prof":
            query = Professor.objects.all()
            lookupType = "staff"
        elif lookup == "ta":
            query = TA.objects.all()
            lookupType = "staff"
        elif lookup == "course":
            query = Course.objects.all()
            lookupType = "course"
        elif lookup == "lab":
            query = Lab.objects.all()
            lookupType = "lab"
        elif lookup == "labToCourse":
            query = LabToCourse.objects.all()
            lookupType = "assignment"
        elif lookup == "profToCourse":
            query = ProfessorToCourse.objects.all()
            lookupType = "assignment"
        elif lookup == "taToCourse":
            query = TAToCourse.objects.all()
            lookupType = "assignment"
        elif lookup == "taToLab":
            query = TAToLab.objects.all()
            lookupType = "assignment"

        if query is None:
            return render(request, "dataLookup.html", {'msg': "Invalid Lookup Type"})
        else:
            return render(request, "dataLookup.html", {"query": query, "lookupType": lookupType})


class ArchiveUser(View):
    def get(self, request):
        # the following if else statement check if someone is logged in or not
        # if logged and the user is not admin
        # the person will get redirected to logging page
        if 'role' in request.session:
            role = request.session['role']
            if role != 'admin':
                messages.add_message(request, messages.INFO, 'Please logging as Admin')
                return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Please logging as Admin')
            return redirect('/')

        # TODO: make sure right html page
        return render(request, "archiveacc.html")

    def post(self, request):
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        accType = request.POST['accType']
        account = Admin.getUser(self, username)
        temp = Admin.archiveAccount(self, account)
        if temp is None:
            return render(request, "archiveacc.html",
                          {'msg': "Failed to archive account. Double check the information entered"})
        else:
            return render(request, "archiveacc.html", {'msg': "Success! Archived account."})


# for people to edit their own contact info.
class EditAccount(View):
    def get(self, request):
        # the following if else statement check if someone is logged in or not
        # if logged and the user is not admin
        # the person will get redirected to logging page
        if 'role' in request.session:
            role = request.session['role']
            username = request.session['user']
            if role == 'professor':
                query = Professor.objects.get(username=username)
                return render(request, "contactinfoProf.html", {'user': query})
            elif role == 'ta':
                query = TA.objects.get(username=username)
                return render(request, "contactinfoTA.html", {'user': query})
            elif role == 'admin':
                query = Admin.objects.get(username=username)
                return render(request, "contactinfoAdmin.html", {'user': query})
            else:
                return render(request, "/")

    def post(self, request):
        username = request.POST['username']
        mailAdrs = request.POST['mailAdrs']
        phNumber = request.POST['phNumber']
        user = Admin.getUser(self, username)

        if type(user) == Professor:
            temp = Professor.EditContact(self, username=username, phNumber=phNumber, mailAdrs=mailAdrs)
            if temp is None:
                return render(request, "contactinfoProf.html", {'msg': "Error editing account. Check current username"})
            else:
                return render(request, "contactinfoProf.html", {'msg': "Success! Account info updated."})

        elif type(user) == TA:
            temp = TA.EditContact(self, username=username, phNumber=phNumber, mailAdrs=mailAdrs)
            if temp is None:
                return render(request, "contactinfoTA.html", {'msg': "Error editing account. Check current username"})
            else:
                return render(request, "contactinfoTA.html", {'msg': "Success! Account info updated."})

        elif type(user) == Admin:
            temp = Admin.EditContact(self, username=username, phNumber=phNumber, mailAdrs=mailAdrs)
            if temp is None:
                return render(request, "contactinfoAdmin.html",
                              {'msg': "Error editing account. Check current username"})
            else:
                return render(request, "contactinfoAdmin.html", {'msg': "Success! Account info updated."})
        else:
            return render(request, "contactinfoAdmin.html", {'msg': "Error editing account. Check current username"})


class AdminEditAccount(View):
    def get(self, request):
        if 'role' in request.session:
            role = request.session['role']
            if role != 'admin':
                messages.add_message(request, messages.INFO, 'Please login as Admin')
                return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Please login as Admin')
            return redirect('/')

        return render(request, "editacc.html")

    def post(self, request):
        fullName = request.POST['fullName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        phNumber = request.POST['phNumber']
        mailAdrs = request.POST['mailAdrs']

        currUser = Staff.getUser(self, username)

        if currUser is None:
            return render(request, "editacc.html", {'msg': "Account doesn't exist."})
        else:
            currUser.username = username
            currUser.email = email
            currUser.password = password
            currUser.phNumber = phNumber
            currUser.mailAdrs = mailAdrs
            currUser.fullName = fullName
            currUser.save()
            return render(request, "editacc.html", {'msg': "Account information has been updated"})
            print(currUser)
