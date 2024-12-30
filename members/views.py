from django.shortcuts import render, HttpResponse

# Create your views here.

def members(request):
    return render(request, "base.html")