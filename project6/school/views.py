from django.shortcuts import render
from school.models import student
from django.db.models import Avg, Sum, Min, Max, Count, Q
from django.views import View

# Create your views here.

# import csv
# lst=[*csv.DictReader(open('/home/programmer/code/django/project6/school/data.csv'))]

# methods which return Query set

def home(request):
    data = student.objects.all()
    # data = student.objects.all()[0:10]
    # print(data)

    # see sql query
    # print(data.query)

    # filter
    # data = student.objects.filter(School='GP')
    # data = student.objects.filter(Age='22')
    # data = student.objects.filter(School='GP').filter(Age=15)

    # exclude
    # data = student.objects.exclude(Age=15)

    # order by

    # for increasing order
    # data = student.objects.order_by('Age')

    # for decreasing order
    # data = student.objects.order_by('-Age')
    # data = student.objects.order_by('Age').reverse()[:10]
    
    # for randomly
    # data = student.objects.order_by('?')

    # for values
    # data = student.objects.values()
    # to get specific columns
    # data = student.objects.values('School')

    # to get tuple
    # data = student.objects.values_list()
    # data = student.objects.values_list('id','School')
    # data = student.objects.values_list('id','School',named=True)

    # data = student.objects.defer('School')
    # data = student.objects.only('School')

    print(data.query)
    return render(request, 'school/home.html',{'data':data})


# methods which donot return Query set

def home1(request):
    # try:
    #     data = student.objects.get(School='GP')
    # except:
    #     data = None

    # data = student.objects.order_by('School').first()
    # data = student.objects.latest('Age')
    # data = student.objects.earliest('Age')
    
    # create an object
    # data = student.objects.create(School=data.School, Sex=data.Sex, Age=data.Age + 1, Mjob=data.Mjob, Fjob=data.Fjob, Reason=data.Reason, Guardian=data.Guardian, Paid=data.Paid)

    # get or create
    # data, created = student.objects.get_or_create(School=data.School, Sex=data.Sex, Age=data.Age + 1, Mjob=data.Mjob, Fjob=data.Fjob, Reason=data.Reason, Guardian=data.Guardian, Paid=data.Paid)

    # update data
    # data = student.objects.filter(pk=10).update(School='Hello')

    # update or create
    # data, created = student.objects.update_or_create(id=10,School='hello1',defaults={'School':'MG'})

    # create in bulk
    # data = student.objects.bulk_create(objs)

    # update in bulk
    # all_data = student.objects.all()
    # data = student.objects.bulk_update(all_data, ['School'])
    
    # in bulk
    # data = student.objects.in_bulk([1,2])

    # delete single row
    # data = student.objects.get(pk=19).delete()

    # to delete all
    # data = student.objects.all().delete()

    data = student.objects.get(pk=10)
    

    return render(request, 'school/home1.html',{'data':data})

def home2(request):

    data = student.objects.filter(School__exact='Hello')
    # for case insensitive
    # data = student.objects.filter(School__iexact='hello')

    # data = student.objects.filter(School__contains='H')
    # data = student.objects.filter(School__icontains='H')

    # data = student.objects.filter(id__in = [1,5,2])

    # greater than 5
    # data = student.objects.filter(id__gt = 5)
    # for less
    # data = student.objects.filter(id__lt = 5)

    # greater than or equal
    # data = student.objects.filter(id__gte = 5)
    # for less or equal
    # data = student.objects.filter(id__lte = 5)

    # data = student.objects.filter(School__startwith = 'H')
    # data = student.objects.filter(School__istartwith = 'H')

    # data = student.objects.filter(School__endswith = 'H')
    # data = student.objects.filter(School__iendswith = 'O')

    # data = student.objects.filter(date__range = ('2020-04-14','2020-08-14'))

    print(data.query)
    return render(request, 'school/home.html',{'data':data})

def home3(request):

    # data = student.objects.aggregate(Avg('Age'))
    # print(data)
    # data = student.objects.aggregate(Sum('Age'))
    # print(data)
    # data = student.objects.aggregate(Min('Age'))
    # print(data)
    # data = student.objects.aggregate(Max('Age'))
    # print(data)
    # data = student.objects.aggregate(Count('Age'))
    # print(data)
    # data = student.objects.filter(School__exact='Hello')

    # data = student.objects.filter(Q(id=3) & Q(School='Hello'))
    # data = student.objects.filter(Q(id=3) | Q(School='Hello'))
    data = student.objects.filter(~Q(School='GP'))


    print(data.query)
    return render(request, 'school/home.html',{'data':data})


class Myview(View):

    def get(self, request):
        print('get request')
        return render(request, 'school/home.html')
    
    def post(self, request):
        print('post request')
        return render(request, 'school/home.html')
    
