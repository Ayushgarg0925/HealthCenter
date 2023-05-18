from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from Health.forms import PatientForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'Health/index.html')

def about(request):
    return render(request,'Health/about.html')

def doctor(request):
    return render(request,'Health/doctor.html')

def news(request):
    return render(request,'Health/news.html')

def contact(request):
    return render(request,'Health/contact.html')

def appointment(request):

    if request.method=="POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/appointment")
    else:
        form=PatientForm()
        return render(request, 'Health/appointment.html',{'form':form})
