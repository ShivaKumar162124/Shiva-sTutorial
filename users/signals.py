from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TutorProfile, StudentProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Depending on user role selection (you'll capture this on signup)
        # For now example: create StudentProfile by default
        StudentProfile.objects.create(user=instance)