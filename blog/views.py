from django.shortcuts import render, get_object_or_404
from .models import Article

# عرض المقالات في الصفحة الرئيسية
def blog_view(request):
    articles = Article.objects.all().order_by('-date_created')
    return render(request, 'blog/article_list.html', {'articles': articles})

# عرض تفاصيل المقالة
def article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article_details.html', {'article': article})



from django.shortcuts import render
from .models import Article  # استبدل Article باسم الموديل الخاص بالمقالات

def home(request):
    latest_articles = Article.objects.order_by('-created_at')[:5]  # جلب آخر 5 مقالات
    return render(request, 'home.html', {'latest_articles': latest_articles})

# عرض آخر 5 مقالات في الصفحة الرئيسية
def home(request):
    latest_articles = Article.objects.order_by('-date_created')[:5]  # جلب آخر 5 مقالات
    return render(request, 'home.html', {'latest_articles': latest_articles})


def home(request):
    latest_articles = Article.objects.order_by('-date_created')[:5]  # جلب آخر 5 مقالات
    print("Latest Articles:", latest_articles)  # طباعة المقالات في الكونسول للتحقق
    return render(request, 'home.html', {'latest_articles': latest_articles})