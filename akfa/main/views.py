from django.shortcuts import render



def first_view(request):
    return render(request, 'home.html')


def first_view2(request):
    return render(request, 'index2.html')