from django.urls import path

from .views import *

urlpatterns = [
    path("", first_view),
    path("ssc/", first_view2)
]