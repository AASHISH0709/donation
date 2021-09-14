from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name='home'),
    path("donate",views.donate,name='donate'),
    path("contact_us",views.contact_us,name='contact_us'),
    path("success",views.success,name='success')
]
