from django.shortcuts import render
from .models import Announcement
import logging

logger = logging.getLogger(__name__)

def landing(request):
    announcement = Announcement.objects.first()
    logger.debug(f"Announcement fetched: {announcement}")
    return render(request, 'main/landing.html', {'announcement': announcement})