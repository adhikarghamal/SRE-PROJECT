from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('chat/', views.chat_view, name='chat'),
    path('send/', views.send_message, name='send_message'),
    path('match-responses/', views.match_and_display_response, name='match_responses'),
]
