from django.shortcuts import render, redirect
from .models import Profile, TechSkill, Comment, Project, Testimonial, ContactMessage, HireMessage
from .forms import ContactForm, HireForm  # Make sure HireForm is imported
from django.http import HttpResponseRedirect
from .models import Comment
from .forms import CommentForm


def index(request):
    profile = Profile.objects.first()
    tech_skills = TechSkill.objects.all()
    comments = Comment.objects.all()
    return render(request, 'index.html', {
        'profile': profile,
        'tech_skills': tech_skills,
        'comments': comments,
    })

def about(request):
    profile = Profile.objects.first()
    return render(request, 'about.html', {'profile': profile})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def services(request):
    return render(request, 'services.html')

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Manually handle form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            
            # Redirect to a success page
            return redirect('success')  # Make sure 'success' is defined in urls.py

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def hire(request):
    if request.method == 'POST':
        form = HireForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            project_description = form.cleaned_data['project_description']
            budget = form.cleaned_data['budget']
            timeline = form.cleaned_data['timeline']
            HireMessage.objects.create(
                name=name, 
                email=email, 
                project_description=project_description, 
                budget=budget, 
                timeline=timeline
            )
            # Redirect to avoid resubmission
            return redirect('hire')  # Make sure 'hire' is defined in urls.py
    else:
        form = HireForm()

    return render(request, 'hire.html', {'form': form})

def success(request):
    return render(request, 'success.html')  # Create this template for success confirmation


def tech_skills(request):
    # Your view logic here
    return render(request, 'tech_skills.html')


def comments_view(request):
    # Logic for fetching and displaying comments
    return render(request, 'comments.html', {})


def submit_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return HttpResponseRedirect('/success/')  # Redirect after successful submission
    else:
        form = CommentForm()

    return render(request, 'comments.html', {'form': form})

def success(request):
    return render(request, 'success.html')




