from django.shortcuts import render
from django.http import HttpResponse
from display.StationRetrieve import StationRetrieve



# Create your views here.
def index(request):
	bike = StationRetrieve()
	list = bike.bikeRetrieve()
	print(list)

	return HttpResponse("HelloWorld")
