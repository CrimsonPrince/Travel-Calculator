from django.db import models

# Create your models here.
class BikeStation(models.Model):

	name = models.CharField(primary_key=True, max_length=60)
	lat = models.FloatField()
	lng = models.FloatField()
	address = models.CharField(max_length=120)
	status = models.CharField(max_length=60)
	lastUpdate = models.DateTimeField()
	numBikes = models.IntegerField()
	numStands = models.IntegerField()
	availableStands = models.IntegerField()
