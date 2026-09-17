from django.shortcuts import render
from .models import Announcement
import logging
from django.shortcuts import render
from django.http import JsonResponse  # ← This is required for the AI chat

logger = logging.getLogger(__name__)

def landing(request):
    announcement = Announcement.objects.first()
    logger.debug(f"Announcement fetched: {announcement}")
    return render(request, 'main/landing.html', {'announcement': announcement})

def ai_chat(request):
    user_message = request.GET.get('message', '')
    reply = "Hi! 👋 I'm Shiva's Tutorial AI assistant. For any questions about tutoring, volunteering, or the VIP program, please contact us directly on WhatsApp:"
    return JsonResponse({'reply': reply})