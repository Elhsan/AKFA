from django.shortcuts import render, redirect       
from .forms import UserForm, OrderForm
from .usecases import *
from .models import *
from django.contrib import messages 
from django.views.generic import DeleteView

def first_view(request):
    return render(request, 'home.html')

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,
                             f"Welcome to our site {username}!")
            form.save(commit=True)
            return redirect('home_page')
        else:
            messages.error(request,
                           "Please correct the errors below.")
            context = {'form': form}
            return render(request, 'registration/create_user.html', context)

    context = {'form': UserForm()}
    return render(request, 'registration/create_user.html', context)


def first_view2(request):
    form = OrderForm()
    if request.method == 'POST':  
        form = OrderForm(request.POST) 
        if form.is_valid(): 
            form.save(commit=True) 
            return redirect('home_page') 
        else:
            print('ERROR FORM INVALID')
    return render(request, 'index2.html', {'form': form})

def Order(request):
    order = Orders.objects.all()
    return render(request, 'orders.html', {'order': order})


class OrderDetails(DeleteView):
    model = Order
    template_name = 'details_order.html'
    context_object_name = 'orderss'