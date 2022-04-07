from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from . models import Event


# Create your views here.

def all_events(request):
    name = 'MyClub'
    events_list = Event.objects.all()
    return render(request, 'events/events_list.html',{
        'name' : name,
        'events_list' : events_list,
    })



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
