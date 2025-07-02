from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from .forms import MessageForm

from django.shortcuts import render, redirect

def home(request):
    error = ""
    capsule_id = ""

    if request.method == "POST":
        capsule_id = request.POST.get('capsule_id', '').strip()

        if not capsule_id:
            error = "Please enter a capsule ID."
        elif not capsule_id.isdigit():
            error = "Invalid capsule ID. Only numbers allowed, no spaces."
        else:
            return redirect('view_capsule', capsule_id=capsule_id)

    return render(request, 'capsules/home.html', {'error': error, 'capsule_id': capsule_id})

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
        try:
            message = Message.objects.get(id=capsule_id)
        except Message.DoesNotExist:
            error = "Capsule ID not found. Please try again."
            return render(request, 'capsules/home.html', {'error': error, 'capsule_id': capsule_id})

        if message.is_unlocked:
            return render(request, 'capsules/view_unlocked_capsule.html', {'message': message.content})
        
        elif message.is_unlockable():
            return render(request, 'capsules/unlock_capsule.html', {'capsule_id': message.id})
        
        else:
            return render(request, 'capsules/capsule_locked.html', {'capsule_id': message.id, 'unlock_date': message.unlock_date})
        
    else:
        return render(request, 'capsules/home.html')