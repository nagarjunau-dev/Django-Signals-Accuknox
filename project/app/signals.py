import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DemoModel

@receiver(post_save, sender=DemoModel)
def thread_check(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")
