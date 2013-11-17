from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'holiday.views.home', name='home'),
    url(r'^itinerary/', include('itinerary.urls', namespace="itinerary")),
    url(r'^admin/', include(admin.site.urls)),
)
