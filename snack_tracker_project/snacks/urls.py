from django.urls import path
from .views import SnackListView,SnackDetailView,HomePage
urlpatterns = [
    path('',HomePage.as_view(), name='home'),
    path('snacks/',SnackListView.as_view(), name='snacks'),
    path('snacks/<int:pk>',SnackDetailView.as_view(), name='snack_detail'),
    
]