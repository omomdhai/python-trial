from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    name = "Om Dhairyansh"
    email ="omdariyans@gmail.com"
    return render(request,'contactus.html',{'name':name,'email':email})

def Etc1(request):

    userName = "parth"
    userEmail = "parth@gmail.com"

    context = {
        'userName':userName,
        'userEmail':userEmail,
    }
    return render(request,'Etc1.html',context)

def Etc2(request):
    return render(request,'Etc2.html')

def Etc3(request):
    return render(request,'Etc3.html')