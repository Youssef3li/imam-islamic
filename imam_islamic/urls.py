from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
# from news.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path('', include('main.urls')),

    path('', include('main.urls')),  # التطبيق الرئيسي للصفحة الرئيسية
    path("students/", include("students.urls")), # تطبيق الطلاب
    path('', include('courses.urls')),
    path("events/", include("events.urls")),
    path("api/students/", include("students.urls")),
    path('blog/', include('blog.urls')),  # ربط URLs الخاص بتطبيق blog
    path('ckeditor/', include('ckeditor_uploader.urls')),  #رابط الصورة الخاصة بالمقال من لوحة التحكم
    # path('news/', include('news.urls')),  # إضافة رابط تطبيق الأخبار
    path('donate/', include('donations.urls')),  # إضافة رابط تطبيق التبرعات
    path('student-services/', TemplateView.as_view(template_name='student-services.html'), name='student_services'), #صفحة خدمات الطلاب
    path('news/', include('news.urls')),
    path('courses/', include('courses.urls')),  # رابط لعرض الدورات
    


]
 

# إضافة دعم لتحميل الملفات الإعلامية مثل الصور
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# imam_project/urls.py

handler404 = "main.views.custom_404"
handler500 = "main.views.custom_500"
