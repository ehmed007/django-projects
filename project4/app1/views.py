from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# from django.contrib.sessions.models import Session
# Create your views here.   

@cache_page(20)
def home(request):

    data = {'name':'ahmed','age':20}
    cache.set_many(data, 30)
    sv = cache.get_many(data)

    mv = cache.get_or_set('fees',4000,30, version=2)

    # mv = cache.get('movie', 'has_expired')
    # if mv == 'has_expired':
    #     cache.set('movie','money heist', 30)
    #     mv = cache.get('movie')
    
    print(mv)
    return render(request, 'app1/home.html',{'dt':mv,'sv':sv})

def home1(request):
    # cache.delete('movie',version=1)
    return render(request, 'app1/home.html')

def setcookie(request):
    response = render(request, 'app1/setcookie.html')
    response.set_cookie('name','ahmed rasheed')
    return response

def getcookie(request):
    name = request.COOKIES['name']
    name = request.COOKIES.get('name')
    print(name)
    return render(request, 'app1/getcookie.html')

def delcookie(request):
    response = render(request, 'app1/delcookie.html')
    response.delete_cookie('name')
    return response


def setsession(request):
    request.session['name'] = 'Kaaleen bhaiya'
    request.session.set_expiry(5)
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request, 'app1/setsession.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name',default='Guest')
    print(name)
    return render(request, 'app1/getsession.html')

def delsession(request):
    # if 'name' in request.session:
        # del request.session
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'app1/delsession.html')
