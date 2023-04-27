from django.urls import path
from .views import *
#BASEURL= http://127.0.0.1:8000

urlpatterns = [
    path("",index,name='home'),
    path("index.html",index,name='home'),
    path("about.html",about,name='about'),
    path("doctor.html",doctor,name='doctor'),
    path("news.html",news,name='news'),
    path("contact.html",contact,name='contact'),
    path("appointment.html", appointment, name='appointment'),
    path("appointment", appointment, name='appointment'),
]
