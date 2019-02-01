class Station:

	def __init__(self, name, lat, lng):
		self.name = name
		self.lat = lat
		self.lng = lng

	def getLocation(self):
		return self.lat + self.lng


class BikeStation(Station):

	def __init__(self,name,lat,lng, address, status, lastUpdate, numBikes, numStands, availableStands):
		Station.__init__(self,name,lat,lng)
		self.address = address
		self.status = status
		self.lastUpdate = lastUpdate
		self.numBikes = numBikes
		self.numStands = numStands
		self.availableStands = availableStands

	def __str__(self):
		return str(self)
