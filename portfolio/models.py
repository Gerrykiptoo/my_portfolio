from django.db import models
from django.utils import timezone

class Profile(models.Model):
    # your fields here
    pass

class TechSkill(models.Model):
    # your fields here
    pass

class Comment(models.Model):
    # your fields here
    pass

class Project(models.Model):
    # your fields here
    pass

class Testimonial(models.Model):
    # your fields here
    pass

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Automatically set the current time


class HireMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_description = models.TextField()
    budget = models.CharField(max_length=50)
    timeline = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.email}"
