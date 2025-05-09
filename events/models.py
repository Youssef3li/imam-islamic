# from django.db import models

# Create your models here.
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="events_images/", blank=True, null=True)

    def __str__(self):
        return self.title
