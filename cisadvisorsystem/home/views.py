from django.shortcuts import render
from django.http import JsonResponse
from .models import Message, Response


# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def chat_view(request):
    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'home/chat.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Anonymous')
        message_text = request.POST.get('message')
        message = Message.objects.create(name=name, text=message_text)
        return JsonResponse({
            'name': message.name,
            'message': message.text,
            'timestamp': message.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        })
    
def match_and_display_response(request):
    messages = Message.objects.all()
    matched_responses = []

    for message in messages:
        response = Response.objects.filter(question=message.text).first()
        if response:
            matched_responses.append((message.text, response.response1))

    return render(request, 'home/match_responses.html', {'matched_responses': matched_responses})

