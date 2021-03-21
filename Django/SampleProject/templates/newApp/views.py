from django.shortcuts import render
from django.http import HttpResponse
from newApp.models import User
from . import forms
# Create your views here.
def start(req):
    return HttpResponse('<h2>Welcome to our site</h2><br><p>Type home to go for home page</p>')
def home(req):
    return HttpResponse('<h2>Go to /user/ to view the list of current users</h2><br><h2>/form to fill the form</h2>')
# def dyn(req):
#     li = User.objects.order_by('age')
#     ht = {'records':li,'content':'This is the current list of Users'}
#     return render(req,'home.html',context = ht)
def display(req):
    li = User.objects.all()
    dic = {'rec':li,'content':'Current list of all users'}
    return render(req,'newApp/sample.html',context = dic)
# def display_form(req):
#     form_obj = forms.SignUp()
#     if(req.method == 'POST'):
#         form_obj = forms.SignUp(req.POST)
#         if form_obj.is_valid():
#             print('username :',form_obj.cleaned_data['userName'])
#             print('email :',form_obj.cleaned_data['email'])
#             print('opinion :',form_obj.cleaned_data['opinion'])
#         else:
#             print('invalid inputs..')
#     else:
#         print("Not a post form")
#     dicti = {'fill_form':form_obj}
#     return render(req,'newApp/sample.html',context = dicti)
def signup(req):
    obj = forms.SignUp()
    if(req.method == 'POST'):
        obj = forms.SignUp(req.POST)
        if(obj.is_valid()):
            obj.save(commit = True)
            # return home(req)
        else:
            print('Invalid')
    return render(req,'newApp/sample.html',context = {'signup':obj})
