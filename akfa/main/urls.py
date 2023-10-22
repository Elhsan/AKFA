from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from .views import *

urlpatterns = [
    path('register/', registration, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path("", first_view, name='home_page2'),
    path("ssc/", first_view2,  name='home_page')
]