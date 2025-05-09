# donations/forms.py
from django import forms

class DonationForm(forms.Form):
    amount = forms.DecimalField(label="مبلغ التبرع", max_digits=10, decimal_places=2)
    message = forms.CharField(label="رسالة", widget=forms.Textarea, required=False)
    
    PAYMENT_METHODS = [
        ('paypal', 'بايبال'),
        ('credit_card', 'بطاقة ائتمانية'),
        ('cash_on_delivery', 'الدفع عند الاستلام'),
    ]
    
    payment_method = forms.ChoiceField(choices=PAYMENT_METHODS, label="طريقة الدفع")
