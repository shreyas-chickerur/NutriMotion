from django.shortcuts import render
from django.http import HttpResponse

# from .models import MODEL_NAME

# Create your views here.

def index(request):
    return render(request, "auth/login.html")
