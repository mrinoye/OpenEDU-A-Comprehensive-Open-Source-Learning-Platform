from django.shortcuts import render

# Create your views here.
def commChat(request):
    return render(request, 'commChat.html')