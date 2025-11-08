from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import DemoModel
import time
import threading
from django.http import HttpResponse
from django.db import transaction
from .models import TransactionModel

def create_demo(request):
    print("Creating object...")
    start = time.time()
    DemoModel.objects.create(name="Test")
    end = time.time()
    print(f"Request finished in {end - start:.2f} seconds")
    return HttpResponse("Check your console for timings")

def thread_demo(request):
    print(f"Caller thread: {threading.current_thread().name}")
    DemoModel.objects.create(name="ThreadTest")
    return HttpResponse("Check console for thread names")



def transaction_demo(request):
    try:
        with transaction.atomic():
            obj = TransactionModel.objects.create(name="RollbackTest")
            raise ValueError("Force rollback")
    except:
        pass

    exists = TransactionModel.objects.filter(name="RollbackTest").exists()
    print(f"Object exists after rollback? {exists}")
    return HttpResponse(f"Object exists after rollback? {exists}")

