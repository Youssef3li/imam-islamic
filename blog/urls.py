from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog_view'),  # لعرض المقالات
    path('article/<int:article_id>/', views.article_details, name='blog_details'),  # لعرض تفاصيل المقالة


    path('', views.home, name='home'),  # الصفحة الرئيسية لعرض آخر 5 مقالات
    #path('article/<int:article_id>/', views.article_details, name='article_details'),  # عرض تفاصيل المقالة
    path('<int:article_id>/', views.article_details, name='article_detail'),
]




