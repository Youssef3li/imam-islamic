# في ملف news/models.py
from django.db import models

class HomepageImage(models.Model):
    image = models.ImageField(upload_to='homepage_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption or "Homepage Image"


# سليدر

# main/models.py
from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='sliders/')
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="حدد ترتيب الصورة في السليدر")
    active = models.BooleanField(default=True, help_text="تفعيل أو تعطيل السليدر")

    def __str__(self):
        return self.title


# اعلان الصفحة الرئيسية 



# class Advertisement(models.Model):
#     image = models.ImageField(upload_to='ads/', blank=True, null=True)
#     link = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return f"Advertisement - {self.id}"