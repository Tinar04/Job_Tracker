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
                  'notes',
                  'interview_date']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'office_location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'source_of_application': forms.TextInput(attrs={'class': 'form-control'}),
            'job_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'interview_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d',
            ),
        }
