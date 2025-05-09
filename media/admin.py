from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MediaFile

admin.site.register(MediaFile)  # تسجيل النموذج في لوحة الإدارة
