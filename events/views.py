# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Event


def events_list(request):
    events = Event.objects.all()
    return render(request, "events/events_list.html", {"events": events})
