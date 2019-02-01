import requests
from pprint import pprint
from station import Station, BikeStation

API_KEY = "7a424c422928a51113b83518de8ea6d1e0cd3085"
API_BASE = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey="

#https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}

def main():
	r = requests.get(API_BASE + API_KEY)
	print(r.status_code)

	list = []
	for i in r.json():
		tmpStation = BikeStation(i['name'],
		i['position']['lat'], i['position']['lng'],
		i['address'],
		i['status'],
		i['last_update'],
		i['available_bikes'], i['bike_stands'],
		i['available_bike_stands']
		)

		list.append(tmpStation)

	for station in list:
		pprint(station)

main()
