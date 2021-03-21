from django.shortcuts import render
from django.http import HttpResponse
from newApp.models import User
from . import forms
from django.http import HttpRequest
# Create your views here.
def home(req):
    dic = {'before_login':'Go to /login/ to login ','after_login':'New to xxx, go to /signup/ and create one account'}
    return render(req,'newApp/HomePage.html',context = dic)
Person_name = None
def signup(req):
    obj = forms.SignUp()
    if(req.method == 'POST'):
        obj = forms.SignUp(req.POST)
        if(obj.is_valid()):
            Person_name = str(obj.cleaned_data['name'])
            obj.save(commit = True)
            # req = HttpRequest()
            return login(req)
        else:
            print('Invalid')
    return render(req,'newApp/signin_or_signup.html',context = {'signup':obj,'signin':'','errormsg':''})
def login(req):
    obj = forms.LoginForm()
    if(req.method == 'POST'):
        obj = forms.LoginForm(req.POST)
        if(obj.is_valid()):
            li = User.objects.filter(username = obj.cleaned_data['username'])
            if(li[0].pwd == obj.cleaned_data['pwd']):
                dic = {'after_login':'XXX Welcomes you dear '+str(li[0].name),'before_login':''}
                return render(req,'newApp/HomePage.html',context = dic)
            else:
                return render(req,'newApp/.signin_or_signup.html',context = {'signup':obj,'signin':'','errmsg':'Invalid password, Try again'})
    return render(req,'newApp/signin_or_signup.html',context = {'signup':'','signin':obj,'erromsg':''})
