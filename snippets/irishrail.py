import requests
from pprint import pprint
import xml.etree.ElementTree as ET
import pandas as pd
import untangle


API_BASE = "http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML_WithStationType?StationType=D"

#https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}

def main():
	r = requests.get(API_BASE)
	print(r.status_code)



	xml = untangle.parse(API_BASE)
	for train in xml.ArrayOfObjStation.children:
		station_name = train.StationDesc.cdata
		print(station_name)

	#parsed = ET.fromstring(r.content)

	#print(parsed.tag)
	#print(parsed.attrib)

	#for station in parsed:
		#name = station.attrib.get(StationDesc)
		#print(station.tag)
		#print()



main()
