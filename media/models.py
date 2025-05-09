from django.db import models

# Create your models here.
from django.db import models


class MediaFile(models.Model):
    title = models.CharField(max_length=255)  # عنوان الملف
    file = models.FileField(upload_to="uploads/")  # حفظ الملف داخل مجلد 'uploads/'
    uploaded_at = models.DateTimeField(auto_now_add=True)  # تاريخ الرفع

    def __str__(self):
        return self.title
