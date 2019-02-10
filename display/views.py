from django.shortcuts import render
from django.http import HttpResponse
from display.StationRetrieve import StationRetrieve



# Create your views here.
def index(request):
	bike = StationRetrieve()
	list = bike.bikeRetrieve()
	context = {
	"bikes": list
	}

	return render(request, "index.html", context)
