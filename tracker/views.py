from django.shortcuts import render, redirect, get_object_or_404

from tracker.models import JobApplication
from .forms import JobApplicationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def index(request):
    statuses = ['applied', 'review', 'shortlisted', 'interview_scheduled', 
                'interview_completed', 'offer', 'accepted', 'rejected']
    
    context = {
        status: JobApplication.objects.filter(status=status, user=request.user).count()
        for status in statuses
    }
    return render(request, 'index.html', context)
    

def about(request):
    return render(request, 'AboutUs.html')

def contact(request):
    return render(request, 'Contact.html')

@login_required
def jobs_by_status(request,status):
    obj = JobApplication.objects.filter(status=status, user=request.user)
    return render(request, 'tracker/jobs_by_status.html',{'jobs':obj,'status':status})


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
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def delete_job(request, id):
    job = get_object_or_404(JobApplication, id=id, user=request.user)
    job.delete()
    return redirect('home')

@login_required
def edit_job(request, id):
    job = get_object_or_404(JobApplication, id=id, user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'edit_job.html', {'form': form})


