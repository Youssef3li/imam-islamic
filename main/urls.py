# from django.urls import path
# from .views import home

# urlpatterns = [
#     path("", home, name="home"),  # 🏠 الصفحة الرئيسية
      
# ]

# from django.conf.urls import handler404, handler500
# from django.shortcuts import render

# def custom_404(request, exception):
#     return render(request, "404.html", status=404)

# def custom_500(request):
#     return render(request, "500.html", status=500)

# handler404 = custom_404
# handler500 = custom_500
# 00000000000000000000000000000000000000000000000000000000

# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # الصفحة الرئيسية
    path("about/", views.about, name="about"),  # صفحة من نحن
    path("students_services/", views.students_services, name="students_services"),  # صفحة خدمات الطلاب
    path("contact/", views.contact, name="contact"),  # صفحة تواصل معنا
    path("login/", views.login, name="login"),# صفحة تسجيل الدخول
    path("article_list.html/", views.blog, name="blog"),
    path("##/", views.contact, name="##"),
    path("##/", views.contact, name="##"),
    path("##/", views.contact, name="##"),
]



# 00000000000000000000000000000000000000000000000000000000
# سليدر

# main/urls.py
# from django.urls import path
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),  # الصفحة الرئيسية
# ]
