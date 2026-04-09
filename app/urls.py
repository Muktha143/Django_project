from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('user_list/', views.user_list, name='user_list'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('user/<int:pk>/edit/', views.update_user, name='update_user'),
    path('user/<int:pk>/delete/', views.delete_user, name='delete_user'),
    path('aadhaar/<str:aadhaar>/', views.aadhaar_card, name='aadhaar_card'),
    path('pan/<str:pan>/', views.pan_card, name='pan_card'),
]