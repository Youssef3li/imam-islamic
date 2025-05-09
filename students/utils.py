import pandas as pd
from django.core.exceptions import ValidationError
from .models import StudentResult


def upload_student_results(file_path):
    """تحميل بيانات الطلاب من ملف إكسل"""
    try:
        df = pd.read_excel(file_path)
        required_columns = {
            "student_id",
            "student_name",
            "subject",
            "grade",
            "exam_year",
        }

        # ✅ التأكد من وجود الأعمدة المطلوبة
        if not required_columns.issubset(df.columns):
            missing_cols = required_columns - set(df.columns)
            raise ValidationError(
                f"الملف لا يحتوي على الأعمدة المطلوبة: {missing_cols}"
            )

        student_results = [
            StudentResult(
                student_id=row["student_id"],
                student_name=row["student_name"],
                subject=row["subject"],
                grade=row["grade"],
                exam_year=int(row["exam_year"]),
            )
            for _, row in df.iterrows()
        ]

        # ✅ إدخال البيانات في قاعدة البيانات دفعة واحدة
        if student_results:
            StudentResult.objects.bulk_create(student_results, ignore_conflicts=True)
            print(f"✅ تمت إضافة {len(student_results)} سجل بنجاح!")
        else:
            print("⚠️ لم يتم العثور على بيانات صالحة للإضافة.")

    except Exception as e:
        print(f"❌ حدث خطأ أثناء معالجة الملف: {e}")
