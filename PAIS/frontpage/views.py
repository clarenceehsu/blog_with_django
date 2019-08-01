from django.shortcuts import render
import time

# Create your views here.

def index(request):
    hour = time.localtime(time.time())[3]
    return render(request, "frontpage.html", context = {'hour': hour})