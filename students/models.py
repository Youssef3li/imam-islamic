from django.db import models
import pandas as pd
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class StudentResult(models.Model):
    student_id = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    exam_year = models.IntegerField()

    class Meta:
        unique_together = ("student_id", "subject", "exam_year")  # منع التكرار

    def __str__(self):
        return f"{self.student_name} - {self.subject} ({self.exam_year})"


class StudentResultFile(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """التحقق من صحة الملف قبل الحفظ"""
        if not self.file.name.endswith((".xls", ".xlsx")):
            raise ValidationError("يجب أن يكون الملف بصيغة Excel (.xls أو .xlsx)")

    def save(self, *args, **kwargs):
        self.clean()  # التأكد من صحة الملف قبل الحفظ
        super().save(*args, **kwargs)  # حفظ الملف أولًا
        self.process_file()  # معالجة الملف بعد الحفظ

    def process_file(self):
        """قراءة البيانات من ملف إكسل وإدخالها في قاعدة البيانات"""
        file_path = self.file.path
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

            # ✅ استبدال القيم الفارغة بسنة افتراضية وبـ "غير متوفر"
            current_year = now().year
            df["exam_year"] = df["exam_year"].fillna(current_year).astype(int)
            df = df.fillna("غير متوفر")

            student_results = []
            for _, row in df.iterrows():
                try:
                    student_results.append(
                        StudentResult(
                            student_id=row["student_id"],
                            student_name=row["student_name"],
                            subject=row["subject"],
                            grade=row["grade"],
                            exam_year=int(row["exam_year"]),
                        )
                    )
                except Exception as row_error:
                    print(f"⚠️ خطأ في السطر {_}: {row_error}")

            # ✅ إدخال البيانات مع تخطي الأخطاء
            if student_results:
                StudentResult.objects.bulk_create(
                    student_results, ignore_conflicts=True
                )
                print(f"✅ تمت إضافة {len(student_results)} سجل بنجاح!")
            else:
                print("⚠️ لم يتم العثور على بيانات صالحة للإضافة.")

        except Exception as e:
            print(f"❌ حدث خطأ أثناء معالجة الملف: {e}")
