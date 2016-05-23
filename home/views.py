from django.shortcuts import render,redirect
# Create your views here.
from django.conf import settings
from django.contrib.auth import logout as logot
from django.contrib.auth import login as logn
from django.contrib.auth import authenticate
def chat(request):
    if not request.user.is_authenticated:
        return redirect('%s' % ('login/'))
    else:        
        return render(request,'home/chat.html')
        
def logout(request):
    logot(request)
    return render(request,'registration/logout.html')
    
    

