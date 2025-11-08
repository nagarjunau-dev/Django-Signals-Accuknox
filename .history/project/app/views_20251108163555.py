from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import DemoModel
import time

def create_demo(request):
    print("Creating object...")
    start = time.time()
    DemoModel.objects.create(name="Test")
    end = time.time()
    print(f"Request finished in {end - start:.2f} seconds")
    return HttpResponse("Check your console for timings")
