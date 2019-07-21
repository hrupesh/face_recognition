from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.

def register(request): 
  
    if request.method == 'POST': 
        form = UserForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return render(request,'register.html',{'msg':'Uploaded Succesfully','status':'success'}) 
    else: 
        form = UserForm() 
    return render(request, 'register.html', {'form' : form , 'msg':''})