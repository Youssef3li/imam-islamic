from django.urls import path
from .views import student_results_page

urlpatterns = [
    path("results/", student_results_page, name="student_results"),
]
