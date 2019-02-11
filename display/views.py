from django.shortcuts import render
from django.http import HttpResponse
from display.StationRetrieve import StationRetrieve



# Create your views here.
def index(request):
	stations = StationRetrieve()
	bikes = stations.bikeRetrieve()
	rail = stations.railRetrieve()
	context = {
	"bikes": bikes,
	"rail" : rail
	}

	return render(request, "index.html", context)
