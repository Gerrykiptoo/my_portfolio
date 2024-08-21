from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    path('hire/', views.hire, name='hire_me'),
    path('success/', views.success, name='success'),
    path('tech-skills/', views.tech_skills, name='tech_skills'),
    path('comments/', views.comments_view, name='comments'),
    path('submit_comment/', views.submit_comment, name='submit_comment')
]