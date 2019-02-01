class Station:

	def __init__(self, name, lat, long):
		self.name = name
		self.lat = lat
		self.long = long

	def getLocation(self):
		return self.lat + self.long


class BikeStation(Station):

	def __init__(self,name,lat,long, address, status, lastUpdate, numBikes, numStands, availableStands):
		Station.__init__(self,name,lat,long)
		self.address = address
		self.status = status
		self.lastUpdate = lastUpdate
		self.numBikes = numBikes
		self.numStands = numStands
		self.availableStands = availableStands
