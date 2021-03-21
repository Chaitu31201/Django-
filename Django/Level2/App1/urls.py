from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.http import HttpResponse
from App1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^user/',views.user,name = 'loginpage'),
    url(r'^new/',views.new,name = 'signup'),
    url(r'^$',views.home,name = 'home'),
    url(r'^user_table/',views.dyn,name = 'user_table')
]
