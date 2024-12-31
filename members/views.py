from django.shortcuts import render
from .models import Member
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, "home.html")

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

def testing(request):
    mymembers = Member.objects.all()
    values = Member.objects.all().values()
    firstnames = Member.objects.all().values_list('firstname')
    firstnamesFlat = Member.objects.all().values_list('firstname', flat=True)
    bobOrLinda = Member.objects.filter(Q(firstname='Bob') | Q(firstname="Linda")).values()
    startsWithL = Member.objects.filter(firstname__startswith='L').values()
    sortedMembers = Member.objects.order_by('firstname').values()
    sortedMembersDesc = Member.objects.order_by('-firstname').values()
    multisort = Member.objects.order_by('lastname', '-id').values()
    context = {
        'mymembers': mymembers,
        'values': values,
        'firstnames': firstnames,
        'firstnamesFlat': firstnamesFlat,
        'bobOrLinda': bobOrLinda,
        'startsWithL': startsWithL,
        'sortedMembers': sortedMembers,
        'sortedMembersDesc': sortedMembersDesc,
        'multisort': multisort
    }
    return render(request, "template.html", context)