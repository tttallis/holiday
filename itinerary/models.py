from django.db import models
from django.core.urlresolvers import reverse

class Day(models.Model):
    date = models.DateField()
    locations = models.ManyToManyField('cities.City', blank=True, null=True, through='DayLocation')
    
    def __unicode__(self):
        return self.date.isoformat()
        
    def get_absolute_url(self):
        return reverse('itinerary:day', kwargs={'year':self.date.year, 'month': self.date.month, 'daynum': self.date.day})        
    
class DayLocation(models.Model):
    day = models.ForeignKey('Day')
    location = models.ForeignKey('cities.City')
    arrival = models.TimeField(blank=True, null=True)
    departure = models.TimeField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
