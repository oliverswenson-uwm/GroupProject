from django.views import View
from django.shortcuts import render
from .models import Lab, Course, Staff

#TODO: make more specific get/post methods

#HOMEPAGE
class Home(View):
    def get(self,request):
        return render(request,"index.html")
    def post(self,request):
        return render(request,"index.html")

#ADMINPAGE
class AdminPage(View):
    def get(self,request):
        return render(request,"adminpage.html")
    def post(self,request):
      pass

#ASSIGNUSER
class AssignUser(View):
    def get(self,request):
        return render(request, "assignuser.html")
    def post(self,request):
        pass

#CREATECOURSE
class CreateCourse(View):
    def get(self, request):
        return render(request, "createcourse.html")
    def post(self, request):
        pass

#NEWACC
class NewAcc(View):
    def get(self, request):
        return render(request, "newacc.html")
    def post(self, request):
        pass

#PROFPAGE
class ProfPage(View):
    def get(self, request):
        return render(request, "profpage.html")
    def post(self, request):
        pass

#TA PAGE
class TaPage(View):
    def get(self, request):
        return render(request, "tapage.html")
    def post(self, request):
        pass