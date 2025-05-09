from django.urls import path
from .views import media_list, upload_media

urlpatterns = [
    path("", media_list, name="media_list"),
    path("upload/", upload_media, name="upload_media"),
]
