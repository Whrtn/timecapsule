from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Message(models.Model):
    content = models.TextField()
    unlock_date = models.DateTimeField()
    secret_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_unlocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_unlockable(self):
        return timezone.now() >= self.unlock_date
    
    def __str__(self):
        return f"Message {self.id}"