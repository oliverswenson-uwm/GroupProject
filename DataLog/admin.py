from django.contrib import admin
from DataLog.models import Admin, Professor, TA, Course, Lab, LabToCourse, ProfessorToCourse, TAToCourse, TAToLab, Assignment

# Register your models here.
admin.site.register(Admin)
admin.site.register(Professor)
admin.site.register(TA)
admin.site.register(Course)
admin.site.register(Lab)
admin.site.register(LabToCourse)
admin.site.register(ProfessorToCourse)
admin.site.register(TAToCourse)
admin.site.register(TAToLab)
admin.site.register(Assignment)