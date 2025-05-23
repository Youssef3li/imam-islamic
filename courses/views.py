# views.py
from django.shortcuts import render, get_object_or_404
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    episodes = course.episodes.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'episodes': episodes})
