# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def media_home(request):
#     return HttpResponse("مرحبًا بك في صفحة الميديا!")
from django.shortcuts import render, redirect
from .models import MediaFile
from .forms import MediaFileForm


def media_list(request):
    files = MediaFile.objects.all()
    return render(request, "media/media_list.html", {"files": files})


def upload_media(request):
    if request.method == "POST":
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("media_list")
    else:
        form = MediaFileForm()
    return render(request, "media/upload_media.html", {"form": form})
