from django.contrib import admin
from django.urls import path
from first_app import views
from django.conf.urls import url
urlpatterns = [
    url(r'^SignUp/',views.signup,name = 'index'),
    url(r'^SignIn/',views.login,name = 'login page'),
    url(r'^$',views.index,name = 'home'),
    path('admin/', admin.site.urls)
]
