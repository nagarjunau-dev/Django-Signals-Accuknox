from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import DemoModel
import time
import threading

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
