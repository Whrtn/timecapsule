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
            return render(request, 'capsules/capsule_created.html', {'secret_code': message.secret_code})
    else:
        form = MessageForm()
    return render(request, 'capsules/create_capsule.html', {'form': form})

# def submit_message(request):
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save()
#             return render(request, 'capsules/message_submitted.html', {'secret_code': message.secret_code})
#     else:
#         form = MessageForm()
#     return render(request, 'capsules/submit_message.html', {'form': form})

# def view_message(request):
#     if request.method == 'POST':
#         secret_code = request.POST.get('secret_code')
#         try:
#             message = Message.objects.get(secret_code=secret_code)
#         except Message.DoesNotExist:
#             return render(request, 'capsules/message_not_found.html')

#         if not message.is_unlockable():
#             return render(request, 'capsules/message_locked.html', {'unlock_date': message.unlock_date})
        
#         return render(request, 'capsules/view_message.html', {'message': message})

#     return render(request, 'capsules/enter_secret_code.html')

# def all_messages(request):
#     messages = Message.objects.all()
#     return render(request, 'capsules/list_all_messages.html', {'messages': messages})
