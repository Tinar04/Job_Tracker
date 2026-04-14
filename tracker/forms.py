from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company_name',
                  'role',
                  'status',
                  'office_location',
                  'salary',
                  'source_of_application',
                  'job_description',
                  'notes']