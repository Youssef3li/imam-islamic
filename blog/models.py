# from django.db import models
# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField

# class Article(models.Model):
#     title = models.CharField(max_length=255)
#     content = RichTextUploadingField()  # ده الحقل اللي هيخليك تكتب المقال بتنسيق
#     date_created = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='articles/', blank=True, null=True)  # إضافة حقل الصورة
    

#     def __str__(self):
#         return self.title

# content = RichTextField()  # ده الحقل اللي هيخليك تكتب المقال بتنسيق
# content = models.TextField()





from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()  # ده الحقل اللي هيخليك تكتب المقال بتنسيق
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)  # إضافة حقل الصورة
    
    def __str__(self):
        return self.title

