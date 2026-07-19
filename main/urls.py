from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('ai-chat/', views.ai_chat, name='ai_chat'),
]