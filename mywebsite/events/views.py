from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue, App


# Create your views here.

def all_events(request):
    name = 'MyClub'
    events_list = Event.objects.all()


    return render(request, 'events/events_list.html',{
        'name' : name,
        'events_list' : events_list,
    })

def show_event(request, event_id):
    event = Event.objects.get(pk=event_id)

    return render(request, 'events/show_blogs.html',
                  {'event':event})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'Joy'
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    current_year = now.year

    return render(request, 'events/home.html', {
        'name': name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
    })


def apps(request):
    apps_list = App.objects.all()

    return render(request, 'events/apps.html',
                  {'apps_list':apps_list})