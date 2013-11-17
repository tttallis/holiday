from django.conf.urls import patterns, include, url

urlpatterns = patterns('itinerary.views',
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<daynum>\d{1,2})/$', 'day', name='day'),
)