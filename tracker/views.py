from django.shortcuts import render, redirect
from django.http import HttpResponse
from tracker.models import JobApplication
from .forms import JobApplicationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def index(request):
    context = {
        'applied':JobApplication.objects.filter(status = 'applied',user = request.user).count(),
        'rejected':JobApplication.objects.filter(status = 'rejected',user = request.user).count(),
        'pending':JobApplication.objects.filter(status = 'pending',user = request.user).count()
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'AboutUs.html')

def contact(request):
    return render(request, 'Contact.html')

@login_required
def applied(request):
    obj = JobApplication.objects.filter(status='applied',user = request.user)
    return render(request, 'Applied.html', {'jobs': obj})
@login_required
def Rejected(request):
    obj = JobApplication.objects.filter(status='rejected',user = request.user)
    return render(request, 'Rejected.html', {'jobs': obj})
@login_required
def Pending(request):
    obj = JobApplication.objects.filter(status='pending',user = request.user)
    return render(request, 'Pendding.html', {'jobs': obj})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = JobApplicationForm()
    return render(request, 'Add_job.html', {'form': form})

def register(request):

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                print(form.errors)
        else:
            form  = UserCreationForm()
        return render(request,'register.html',{'form':form})


@login_required
def delete_job(request,id):
    job = JobApplication.objects.get(id = id, user  = request.user)
    job.delete()
    return redirect('home')
        

@login_required
def edit_job(request,id):
    job = JobApplication.objects.get(id =id,user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = JobApplicationForm(instance = job)
    return render(request,'edit_job.html',{'form':form})


