from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_news_view, name='news_list'),
    path('events/', views.events_view, name='events_list'),
]
