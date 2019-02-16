import requests
import untangle
from display.models import BikeStation

class StationRetrieve():

	def bikeRetrieve(self):
		API_KEY = "7a424c422928a51113b83518de8ea6d1e0cd3085"
		API_BASE = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey="

		r = requests.get(API_BASE + API_KEY)
		print(r.status_code)

		stationList = []
		for i in r.json():
			tmpStation = BikeStation(i['name'],
			i['position']['lat'], i['position']['lng'],
			i['address'],
			i['status'],
			i['last_update'],
			i['available_bikes'], i['bike_stands'],
			i['available_bike_stands']
			)
			stationList.append(tmpStation)

		return stationList

	def railRetrieve(self):
		API_BASE = "http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML"
		r = requests.get(API_BASE)
		print(r.status_code)


		stationList = []
		xml = untangle.parse(API_BASE)
		for train in xml.ArrayOfObjStation.children:
			if float(train.StationLatitude.cdata) == 0:
				continue
			tmpStation = BikeStation(train.StationDesc.cdata, train.StationLatitude.cdata, train.StationLongitude.cdata)
			stationList.append(tmpStation)

		return stationList
