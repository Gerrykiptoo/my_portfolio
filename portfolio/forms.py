# portfolio/views.py
from django.shortcuts import render
from .models import Profile, TechSkill, Comment, Project, Testimonial, ContactMessage
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class HireForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    project_description = forms.CharField(widget=forms.Textarea, required=False)  # Include this field
    
    
    
    
    