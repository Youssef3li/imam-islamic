from django.shortcuts import render
from .models import News, Event
from datetime import date

def all_news_view(request):
    all_news = News.objects.order_by('-date')
    return render(request, 'news/all_news.html', {'all_news': all_news})


def events_view(request):
    upcoming_events = Event.objects.filter(date__gte=date.today()).order_by('date')
    past_events = Event.objects.filter(date__lt=date.today()).order_by('-date')
    return render(request, 'news/events.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events
    })
