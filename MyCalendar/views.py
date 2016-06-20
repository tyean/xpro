from django.views import generic
from .models import Event
from django.shortcuts import render
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar
from datetime import date, datetime
from itertools import groupby
from django.utils.timezone import now
from django.utils.html import conditional_escape as esc
from calendar import monthrange

#class EventView(generic.ListView):
#    template_name = 'MyCalendar/Event.html'

def aboutUsView(request):
    return render(request, 'MyCalendar/AboutUs.html')

class EventCalendar(HTMLCalendar):

    def __init__(self, events):
        super(EventCalendar, self).__init__()
        self.events = self.group_by_day(events)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.events:
                cssclass += ' filled'
                body = ['<ul>']
                for event in self.events[day]:
                    body.append('<li>')
                    #body.append('<a href="%s">' % event.get_absolute_url())
                    body.append(esc(event.event_name))
                    body.append('</li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, self).formatmonth(year, month)

    def group_by_day(self, events):
        field = lambda event: event.start_date.day
        return dict(
            [(day, list(items)) for day, items in groupby(events, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)

def named_month(pMonthNumber):
    """
    Return the name of the month, given the month number
    """
    return date(1900, pMonthNumber, 1).strftime('%B')

def home(request):
    """
    Show calendar of events this month
    """
    lToday = datetime.now()
    return calendar(request, lToday.year, lToday.month)

def calendarView(request, year=now().year, month=now().month):
    """
    Show calendar of events for specified month and year
    """
    lYear = int(year)
    lMonth = int(month)
    lCalendarFromMonth = datetime(lYear, lMonth, 1)
    lCalendarToMonth = datetime(lYear, lMonth, monthrange(lYear, lMonth)[1])
    MonthlyEvents = Event.objects.filter(start_date__gte=lCalendarFromMonth, start_date__lte=lCalendarToMonth)
    lCalendar = EventCalendar(MonthlyEvents).formatmonth(lYear, lMonth)
    lPreviousYear = lYear
    lPreviousMonth = lMonth - 1
    if lPreviousMonth == 0:
        lPreviousMonth = 12
        lPreviousYear = lYear - 1
    lNextYear = lYear
    lNextMonth = lMonth + 1
    if lNextMonth == 13:
        lNextMonth = 1
        lNextYear = lYear + 1
    lYearAfterThis = lYear + 1
    lYearBeforeThis = lYear - 1

    return render(request, 'MyCalendar/cal_month.html', {'Calendar' : mark_safe(lCalendar),
                                                       'Month' : lMonth,
                                                       'MonthName' : named_month(lMonth),
                                                       'Year' : lYear,
                                                       'PreviousMonth' : lPreviousMonth,
                                                       'PreviousMonthName' : named_month(lPreviousMonth),
                                                       'PreviousYear' : lPreviousYear,
                                                       'NextMonth' : lNextMonth,
                                                       'NextMonthName' : named_month(lNextMonth),
                                                       'NextYear' : lNextYear,
                                                       'YearBeforeThis' : lYearBeforeThis,
                                                       'YearAfterThis' : lYearAfterThis,
                                                   })