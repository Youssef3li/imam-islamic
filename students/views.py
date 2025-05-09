from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentResult


def student_results_page(request):
    student_id = request.GET.get("student_id", None)  # استلام ID الطالب من الـ URL
    result = None

    if student_id:
        try:
            student = StudentResult.objects.get(student_id=student_id)
            result = {
                "student_name": student.student_name,
                "subject": student.subject,
                "grade": student.grade,
                "exam_year": student.exam_year,
            }
        except StudentResult.DoesNotExist:
            result = {"error": "لم يتم العثور على النتيجة لهذا الطالب"}

    return render(request, "students/student_results.html", {"result": result})
