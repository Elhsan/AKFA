from django.urls import path
from .views import *

urlpatterns = [
    path('', news_home, name='news_home'),
    path('create/', create_order, name='create_order'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', NewsUpdatView.as_view(), name='news_update'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='news_delete'),
]
