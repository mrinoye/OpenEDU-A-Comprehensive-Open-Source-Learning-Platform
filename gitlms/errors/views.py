from django.shortcuts import render

# Create your views here.
def unauthorizedaccess(request):
    return render(request,"unauthorizedaccess.html")

def illegalactivity(request):
    return render(request,"illegalactivity.html")