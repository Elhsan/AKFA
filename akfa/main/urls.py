from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from .views import *

urlpatterns = [
    path('weqqweasdasdwqe/', first_view, name='home_page'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path("", registration, name='register'),
    path("scc/", first_view2,  name='home_page2'),
    path("Order/", Order,  name='Order'),
    path('/order/<int:pk>', OrderDetails.as_view(), name='order-details'),
]