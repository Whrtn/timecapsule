from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from .forms import MessageForm
from django.utils import timezone

def home(request):
    return render(request, 'capsules/home.html')

def create_capsule(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            return render(request, 'capsules/capsule_created.html', {'secret_code': message.secret_code, 'capsule_id': message.id})
    else:
        form = MessageForm()
    return render(request, 'capsules/create_capsule.html', {'form': form})

def view_capsule(request, capsule_id):
    if request.method == 'GET':
        message = get_object_or_404(Message, id=capsule_id)

        if message.is_unlocked:
            return render(request, 'capsules/view_unlocked_capsule.html', {'message': message.content})
        
        elif message.is_unlockable():
            return render(request, 'capsules/unlock_capsule.html', {'capsule_id': message.id})
        
        else:
            return render(request, 'capsules/capsule_locked.html', {'capsule_id': message.id, 'unlock_date': message.unlock_date})
        
    else:
        return render(request, 'capsules/home.html')