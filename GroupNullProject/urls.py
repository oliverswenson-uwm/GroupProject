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
from DataLog import views

urlpatterns = [
    path('admin/', admin.site.urls),#django administration page
    path('', views.Login.as_view()),
    path('supervisor/', views.AdminView.as_view()),
    path('professor/', views.ProfessorView.as_view()),
    path('ta/', views.TaView.as_view()),
    path('createuser/', views.CreateUser.as_view()),
    # path('assignuser/', AssignUser.as_view()),
    # path('createcourse/', CreateCourse.as_view()),
    # path('newaccount/', NewAcc.as_view()),
    # path('profpage/', ProfPage.as_view()),
    # path('tapage/', TaPage.as_view()),
]
