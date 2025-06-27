from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'unlock_date']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400',
                'rows': 4,
                'placeholder': 'Type your message here...'
            }),
            'unlock_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'w-full border border-gray-300 rounded px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),
        }
