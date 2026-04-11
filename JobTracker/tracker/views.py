from django.shortcuts import render,HttpResponse
from tracker.models import JobApplication

# Create your views here.
def index(request):
    context = {
        'variable':"this is sent"
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("this is about us page")

def contact(request):
    return HttpResponse("Call us  -7725067250 ")

def applied(request):
    obj =JobApplication.objects.filter(status = 'applied')
    return render(request,'Applied.html',{'jobs':obj})

def Rejected(request):
    obj = JobApplication.objects.filter(status = 'rejected')
    return render(request,'Rejected.html',{'jobs':obj})

def Pending(request):
    obj = JobApplication.objects.filter(status = 'pending')
    return render(request,'Pendding.html',{'jobs':obj})