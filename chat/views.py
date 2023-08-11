from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

from accounts.views import is_student, is_teacher
@login_required
def user_list(request):
    current_user = request.user
    users = User.objects.exclude(id=current_user.id)
    context = {
        'users': users,
        'teacher':is_teacher(current_user),
        'student':is_student(current_user),
        }
    return render(request, 'chat/inbox.html', context)

@login_required
def chat(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    # Retrieve all messages exchanged between the sender and receiver
    messages_sent = Message.objects.filter(sender=request.user, receiver=receiver)
    messages_received = Message.objects.filter(sender=receiver, receiver=request.user)

    # Combine the sent and received messages and order them by timestamp
    all_messages = (messages_sent | messages_received).order_by('timestamp')

    context = {
        'teacher':is_teacher(request.user),
        'student':is_student(request.user),
        'receiver': receiver,
        'messages': all_messages}
    return render(request, 'chat/chat.html', context)

def send_message(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        sender = request.user
        Message.objects.create(sender=sender, receiver=receiver, content=content)

    return redirect('chat', user_id)