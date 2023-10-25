from django.shortcuts import render, redirect
from .forms import UserForm
from .usecases import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('login')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/create_user.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/create_user.html', context)

def about(request):
    return render(request, 'main/about.html')