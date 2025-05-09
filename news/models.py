from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news_images/')
    date = models.DateField(null=True, blank=True)  # 👈 اضفنا null=True, blank=True
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 👈 حقل التاريخ تلقائي وقت الإنشاء

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    def is_upcoming(self):
        from datetime import date
        return self.date >= date.today()

    def __str__(self):
        return self.name
