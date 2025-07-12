from django.urls import path
from . import views

urlpatterns = [
    path('send/<int:to_user_id>/', views.send_swap_request, name='send_swap_request'),
    path('requests/', views.swap_requests, name='swap_requests'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
    path('accept/<int:pk>/', views.accept_swap, name='accept_swap'),
    path('reject/<int:pk>/', views.reject_swap, name='reject_swap'),
    path('delete/<int:pk>/', views.delete_swap, name='delete_swap'),
    path('feedback/<int:pk>/', views.leave_feedback, name='leave_feedback'),
] 