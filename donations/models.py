from django.db import models

class Donation(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="الاسم الكامل")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ")
    message = models.TextField(blank=True, null=True, verbose_name="رسالة")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.amount} ج.م"
