from django.shortcuts import render
from models import Day
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from datetime import datetime

def day(request, year, month, daynum):
    date = datetime(int(year), int(month), int(daynum))
    day = Day.objects.get(date=date)
    return render_to_response('itinerary/day.html', {
        'day': day,
    }, context_instance=RequestContext(request))
