from django.contrib import admin
from .models import StudentResult, StudentResultFile


class StudentResultAdmin(admin.ModelAdmin):
    list_display = ("student_id", "student_name", "subject", "grade", "exam_year")
    search_fields = ("student_id", "student_name", "subject")
    list_filter = ("subject", "grade", "exam_year")  # فلترة حسب الفرع والمستوي والسنة
    ordering = ("-exam_year", "student_name")  # ترتيب حسب السنة ثم الاسم


class StudentResultFileAdmin(admin.ModelAdmin):
    list_display = ("file", "uploaded_at")  # عرض الملف وتاريخ الرفع
    search_fields = ("file",)


admin.site.register(StudentResult, StudentResultAdmin)
admin.site.register(StudentResultFile, StudentResultFileAdmin)
