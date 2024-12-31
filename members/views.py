from django.shortcuts import render
from .models import Member

# Create your views here.

def members(request):
    mymembers = Member.objects.all()
    context = {
        'mymembers': mymembers
    }
    return render(request, "all_members.html", context)