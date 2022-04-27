from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def profile(request):
    '''this view is for profile updation'''
    u_form = UserUpdateForm()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)  #to get our information already filled in
        if u_form.is_valid():
            u_form.save()
            return redirect('main')
    else:
       u_form = UserUpdateForm(instance=request.user)
    context = {
    'u_form':u_form,
    }
    return render(request,'users/profile.html',context)


def register(request):
    '''This view is for registering the new user.
    It accepts a post request'''
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} you are now able to login')
            return redirect('login')
        form = UserRegisterForm(request.POST)	
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
