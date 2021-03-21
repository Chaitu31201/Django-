from django.shortcuts import render
from django.http import HttpResponse
def signup(request):
    return HttpResponse('<h2>Signup with Google !</h2>')
# Create your views here.
def login(request):
    return HttpResponse('<h2>Enter your username and password</h2>')
def homepage(req):
    return HttpResponse('<h1>Welcome to ZingZang</h1>')
def index(req):
    my_dict = {'dyn_content':'<em>This is the dynamic content</em>'}
    return render(req,'index.html',context = my_dict)
