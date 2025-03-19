from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User
@login_required
# Create your views here.
def departments(request):
    context={'name':request.user.username}

    return render(request,"departments.html",context)

def courses(request):
    context={'name':request.user.username}

    return render(request,"courses.html",context)

def students(request):
    users=User.objects.all()
    context={'name':request.user.username,'users':users}

    return render(request,"students.html",context)