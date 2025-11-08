from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_demo/', views.create_demo),
    path('thread_demo/', views.thread_demo),
    path('transaction_demo/', views.transaction_demo),
]
