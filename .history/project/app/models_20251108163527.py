from django.db import models

# Create your models here.
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
