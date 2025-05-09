from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    episode_count = models.PositiveIntegerField(default=0)  # إضافة قيمة افتراضية
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Episode(models.Model):
    course = models.ForeignKey(Course, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    episode_number = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Episode {self.episode_number} - {self.title}"
