from django.shortcuts import render
from .models import Member

# Create your views here.

def members(request):
    mymembers = Member.objects.all()
    context = {
        'mymembers': mymembers
    }
    return render(request, "all_members.html", context)

def details(request, member_id):
    mymember = Member.objects.get(id=member_id)
    context = {
        'mymember': mymember
    }
    return render(request, "details.html", context)

def home(request):
    return render(request, "home.html")