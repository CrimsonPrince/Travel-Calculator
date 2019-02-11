import requests
from pprint import pprint
import untangle
from station import Station


API_BASE = "http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML"

#https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}

def main():
	r = requests.get(API_BASE)
	print(r.status_code)


	list = []
	xml = untangle.parse(API_BASE)
	for train in xml.ArrayOfObjStation.children:
		tmpStation = Station(train.StationDesc.cdata, train.StationLatitude.cdata, train.StationLongitude.cdata)
		list.append(tmpStation)

	pprint(list)
	#parsed = ET.fromstring(r.content)

	#print(parsed.tag)
	#print(parsed.attrib)

	#for station in parsed:
		#name = station.attrib.get(StationDesc)
		#print(station.tag)
		#print()



main()
