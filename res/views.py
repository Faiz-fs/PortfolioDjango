from django.shortcuts import render,redirect
from django.contrib import messages
from res.models import Message

# Create your views here.

def index(request):
    return render(request,'index.html')

def send(request,val):
    lst=val.split(" ")
    data_pass=Message.objects.create(name=lst[0],email=lst[1],msg=lst[2])
    data_pass.save()
    messages.success(request,"Message sent successfully")
    return redirect('index')
    #return render(request,'index.html',{'data':"Message sent successfully"})
