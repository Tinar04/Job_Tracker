from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path("", views.index,name='home'),
    path("about-us/", views.about,name = 'about'),
    path('contact',views.contact,name='contactus'),
    path('Applied/',views.applied,name = 'appliedIN'),
    path('Rejected/',views.Rejected, name = 'RejectedFrom'),
    path('pending/',views.Pending, name  = 'pending'),
    path('add_job/',views.add_job,name = 'Add_Job'),
    path('register/',views.register,name = 'register'),
    path('delete/<int:id>/', views.delete_job, name='delete_job'),
    path('edit/<int:id>/', views.edit_job, name='edit_job'),
    
]

