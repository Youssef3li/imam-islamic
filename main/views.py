# # في ملف views.py
# from django.shortcuts import render




# # سليدر



# from .models import Slider

# def home(request):
#     sliders = Slider.objects.filter(active=True).order_by('order')  # استرجاع السليدرات النشطة وترتيبها
#     return render(request, 'index.html', {'sliders': sliders})




# # صورة الصفحة الرئيسية 


# from .models import HomepageImage

# def home(request):
#     image = HomepageImage.objects.first()  # ناخد أول صورة من قاعدة البيانات
#     return render(request, 'index.html', {'image': image})



# main/views.py

# from django.shortcuts import render
# from .models import Slider, HomepageImage

# def home(request):
#     sliders = Slider.objects.filter(active=True).order_by('order')
#     image = HomepageImage.objects.first()
    
#     return render(request, 'index.html', {
#         'sliders': sliders,
#         'image': image,
#     })


# # اخر المقالات 
# from django.shortcuts import render
# from blog.models import Article  # التأكد من استيراد المقالات من تطبيق blog

# def home(request):
#     latest_articles = Article.objects.order_by('-date_created')[:6]  # جلب آخر 6 مقالات بناءً على التاريخ
#     return render(request, 'index.html', {'latest_articles': latest_articles})
# # 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

# # main/views.py
# from django.shortcuts import render
# from .models import Slider, HomepageImage
# from blog.models import Article  # استيراد المقالات من تطبيق blog

# def home(request):
#     # جلب السليدرات النشطة وترتيبها
#     sliders = Slider.objects.filter(active=True).order_by('order')
    
#     # جلب أول صورة من قاعدة البيانات
#     image = HomepageImage.objects.first()
    
#     # جلب آخر 6 مقالات
#     latest_articles = Article.objects.order_by('-date_created')[:6]
    
#     # إرسال البيانات إلى الصفحة الرئيسية
#     return render(request, 'index.html', {
#         'sliders': sliders,
#         'image': image,
#         'latest_articles': latest_articles,
#     })

# # 000000000000000000000000000000000000000000000000000
# # main/views.py

# from django.shortcuts import render

# def home(request):
#     return render(request, "index.html")

# def about(request):
#     return render(request, "about.html")

# def students_services(request):
#     return render(request, "students_services.html")

# def contact(request):
#     return render(request, "contact.html")
# def contact(request):
#     return render(request, "login.html")




# # صفحة الخطأ 404
# def custom_404(request, exception):
#     return render(request, "404.html", status=404)

# # صفحة الخطأ 500
# def custom_500(request):
#     return render(request, "500.html", status=500)


# # 000000000000000000000000000000000000000000000000000000000000000000000000000000000
# # اعلان الصفحة الرئيسية 

# # from .models import Advertisement

# # def home(request):
# #     ads = Advertisement.objects.all()  # جلب جميع الإعلانات من قاعدة البيانات
# #     return render(request, 'index.html', {'advertisements': ads})



# # from django.shortcuts import render
# # from news.models import News, Event
# # from datetime import date

# # def home_view(request):
# #     news_list = News.objects.order_by('-date')[:4]
# #     upcoming_events = Event.objects.filter(date__gte=date.today()).order_by('date')[:4]
# #     past_events = Event.objects.filter(date__lt=date.today()).order_by('-date')[:4]

# #     return render(request, 'main/index.html', {
# #         'news_list': news_list,
# #         'upcoming_events': upcoming_events,
# #         'past_events': past_events
# #     })



# main/views.py

from django.shortcuts import render
from .models import Slider, HomepageImage
from blog.models import Article
from news.models import News, Event
from datetime import date


def home(request):
    sliders = Slider.objects.filter(active=True).order_by('order')
    image = HomepageImage.objects.first()
    latest_articles = Article.objects.order_by('-date_created')[:6]
    news_list = News.objects.order_by('-date')[:4]
    upcoming_events = Event.objects.filter(date__gte=date.today()).order_by('date')[:4]
    past_events = Event.objects.filter(date__lt=date.today()).order_by('-date')[:4]

    return render(request, 'index.html', {
        'sliders': sliders,
        'image': image,
        'latest_articles': latest_articles,
        'news_list': news_list,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    })


def about(request):
    return render(request, "about.html")

def students_services(request):
    return render(request, "students_services.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "article_list.html")

# لو عايز صفحة login
def login(request):
    return render(request, "login.html")


# صفحة الخطأ 404
def custom_404(request, exception):
    return render(request, "404.html", status=404)

# صفحة الخطأ 500
def custom_500(request):
    return render(request, "500.html", status=500)
