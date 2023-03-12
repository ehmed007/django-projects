from django.contrib import admin
from .models import student
# Register your models here.

class student_data(admin.ModelAdmin):
    list_display = ('id','School','Sex','Age','Mjob','Fjob','Reason','Guardian','Paid')

admin.site.register(student, student_data)