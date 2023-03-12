from django.shortcuts import render
from school.models import student
# Create your views here.

def home(request):
    # data = student.objects.all()
    data = 'ahmedas'
    return render(request, 'school/home.html',{'data':data})