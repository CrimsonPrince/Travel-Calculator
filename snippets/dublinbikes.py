import requests
from pprint import pprint

API_KEY = "7a424c422928a51113b83518de8ea6d1e0cd3085"
API_BASE = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey="

#https://api.jcdecaux.com/vls/v1/stations?contract={contract_name}&apiKey={api_key}

def main():
	r = requests.get(API_BASE + API_KEY)
	print(r.status_code)

	for station in r.json():
		pprint(station['name'])
		pprint(station['available_bikes'])
		pprint(r.json())


main()
