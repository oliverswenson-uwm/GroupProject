"""GroupNullProject URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DataLog.views import Home, AdminPage, AssignUser, CreateCourse, NewAcc, ProfPage, TaPage

urlpatterns = [
    path('admin/', admin.site.urls),#django administration page
    path('', Home.as_view()),
    path('adminpage/', AdminPage.as_view()),#admin of the scheduling app page
    path('assignuser/', AssignUser.as_view()),
    path('createcourse/', CreateCourse.as_view()),
    path('newaccount/', NewAcc.as_view()),
    path('profpage/', ProfPage.as_view()),
    path('tapage/', TaPage.as_view()),
]
