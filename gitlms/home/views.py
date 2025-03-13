from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def dashboard(request):
    context={'name':request.user.username}

    return render(request,"dashboard.html",context)