
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class DemoModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=DemoModel)
def slow_signal(sender, instance, **kwargs):
    print("Signal started...")
    time.sleep(3)
    print("Signal finished.")




class TransactionModel(models.Model):
    name = models.CharField(max_length=100)
    saved = models.BooleanField(default=False)

@receiver(post_save, sender=TransactionModel)
def mark_saved(sender, instance, **kwargs):
    # Try updating immediately
    instance.saved = True
    instance.save()
    print("Signal updated saved=True")

