# في ملف news/admin.py
from django.contrib import admin
from .models import HomepageImage

admin.site.register(HomepageImage)



# main/admin.py
# سليدر
from .models import Slider

class SliderAdmin(admin.ModelAdmin):
  list_display = ('title', 'order', 'active', 'image')
  list_filter = ('active',)
  search_fields = ('title',)

admin.site.register(Slider, SliderAdmin)



# اعلان الصفحة الرئيسية 

# from .models import Advertisement

# admin.site.register(Advertisement)



