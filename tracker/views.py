from django.shortcuts import render,HttpResponse
from tracker.models import JobApplication
from .forms import JobApplicationForm
from django.shortcuts import render, redirect 
from django.views.decorators.csrf import csrf_exempt

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


def add_job(request):
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = JobApplicationForm()
    return render (request,'add_job.html',{'form':form})