from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import UserForm, ImageForm
from .models import User, Image
from django.contrib import messages
from django.forms import modelformset_factory

# Create your views here.

def register(request): 
    
    ImageFormSet = modelformset_factory(Image,form=ImageForm, extra=2)

    if request.method == 'POST': 
        userform = UserForm(request.POST, request.FILES) 
        formset = ImageFormSet(request.POST, request.FILES,queryset=Image.objects.none())
  
        if userform.is_valid() and formset.is_valid():
            user_form = userform.save(commit=False)
            user_form.save()

            for form in formset.cleaned_data:
                image = form['user_img']
                photo = Image(user=user_form, user_img=image)
                photo.save()
            print("Uploaded")
            messages.success(request,"Data Uploaded Successfully")
            return HttpResponseRedirect('/')
        else:
            print (userform.errors, formset.errors) 
    else: 
        userform = UserForm() 
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'register.html', {'userform' : userform, 'formset':formset , 'msg':''})


def upload(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            user = User(name=name,email=email)
            user.save()
            for file in request.FILES.getlist('user_img'):
                img = Image( user=user,user_img=file)
                img.save()
            return render(request,'register.html',{'msg':'Data Uploaded Successfully','status':'success'})
        except Exception as ex:
            return render(request,'register.html',{'msg':'User already Exists! Try with Different name again.','status':'danger'})
    return HttpResponse("Error")