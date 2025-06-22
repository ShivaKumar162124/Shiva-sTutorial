from django.db import models
from django.contrib.auth.models import User


class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.CharField(max_length=200)
    experience = models.TextField(blank=True)
    # add more fields as needed
    is_tutor = models.BooleanField(default=True)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)
    # add more fields as needed
    is_student = models.BooleanField(default=True)

# Create your models here.
