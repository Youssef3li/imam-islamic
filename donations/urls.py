from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate_view, name='donate'),
    path('success/', views.success_view, name='donation_success'),
]
