from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class JobApplication(models.Model):
    STATUS_CHOICES = [
    ('applied', 'Applied'),
    ('review', 'Under Review'),
    ('shortlisted', 'Shortlisted'),
    ('interview_scheduled', 'Interview Scheduled'),
    ('interview_completed', 'Interview Completed'),
    ('offer', 'Offer Received'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected')]

    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES,default='applied')
    office_location = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    date_of_application = models.DateField(auto_now_add=True)
    source_of_application = models.CharField(max_length=50)
    job_description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-date_of_application']

    def __str__(self):
        return self.company_name