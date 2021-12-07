from django.shortcuts import render, redirect
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
                return render(request, "index.html", {'msg': 'INVALID Username OR Password'})
        else:  # user is None, mean invalid username or password or user does not exist
            request.session.flush()  # log out logged user
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

        return render(request, "tapage.html")

class CreateUser(View):
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

        return render(request, "newacc.html")

    def post(self, request):
        fullName = request.POST['fullName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        phNumber = request.POST['phNumber']
        mailAdrs = request.POST['mailAdrs']
        accType = request.POST['accType']

        # cheacking if input is valid
        for field in request.POST:
            if field == "" or field[0] == " ":
                return render(request, "newacc.html", {'msg': "Failed: A empty field in form"})
        print(request.POST)
        user = Staff.getUser(self, username)
        if not user:  # username does not exits(new user is being created)
            newUser = None
            if accType == 'Admin':
                newUser = Admin.createAdmin(self, fullName, email, username, password, phNumber, mailAdrs)
                print(newUser)
            elif accType == 'Professor':
                newUser = Admin.createProf(self, fullName, email, username, password, phNumber, mailAdrs)
                print(newUser)
            elif accType == 'TA':
                newUser = Admin.createTA(self, fullName, email, username, password, phNumber, mailAdrs)
                print(newUser)
            return render(request, "newacc.html", {'msg': "Success: New Account has been create "})
        else:
            return render(request, "newacc.html", {'msg': "Fail: Username exist, Please Pick a new Username"})


# ASSIGNUSER
class AssignUser(View):
    def get(self, request):
        return render(request, "assignuser.html")

    def post(self, request):
        pass


# CREATECOURSE
class CreateCourse(View):
    def get(self, request):
        return render(request, "createcourse.html", {})

    def post(self, request):
        try:
            m = Course.objects.get(name=request.POST['name'])
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
                Course(name=request.POST['name'], section=request.POST['section'], credits=request.POST['credits'],
                       prereqs=request.POST['prereqs'], description=request.POST['description']).save()
            return render(request, "createcourse.html", {'name': request.POST['name'],
                                                         'section': request.POST['section'],
                                                         'credits': request.POST['credits'],
                                                         'prereqs': request.POST['prereqs'],
                                                         'description': request.POST['description'],
                                                         'msg': "The course has been created."})


# PROFPAGE
class ProfPage(View):
    def get(self, request):
        return render(request, "profpage.html")

    def post(self, request):
        pass


# TA PAGE
class TaPage(View):
    def get(self, request):
        return render(request, "tapage.html")

    def post(self, request):
        pass