from django.views import generic
from .models import Event
from django.shortcuts import render

#class EventView(generic.ListView):
#    template_name = 'MyCalendar/Event.html'

def AboutUsView(request):
    return render(request, 'MyCalendar/AboutUs.html')


