from django.shortcuts import render
from django.http import HttpResponse
from App1.models import User,Guest
# Create your views here.
def user(req):
    dic = {'content':'Login with your username and password'}
    return render(req,'home.html',context = dic)
def new(req):
    dic = {'content':'Create a new account with your Gmail'}
    return render(req,'home.html',context = dic)
def start(req):
    return HttpResponse('<h2>Welcome to our site</h2>')
def home(req):
    return HttpResponse('<h2>This is Home page</h2>')
def dyn(req):
    li = User.objects.order_by('age')
    ht = {'records':li,'content':'This is the current list of Users'}
    return render(req,'home.html',context = ht)
