"""
model storage locations to enable 0(1) lookup
rows are lettered, while locations are numbered
structured as a dictionary of types {char:[string]}
"""
class StorageLocations:
	def create(self,locationsPerRow):
		"""
		type locationsPerRow: int
		rtype: Dictionary(char : List[string])
		"""
		letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		storageLocations = {}
		storageLocations['index'] = letters
		for c in letters:
			storageLocations[c] = [None]*locationsPerRow
		return storageLocations
		
"""
the goal of this module is to take a list of skus and
a set of locations, and to populate the locations with
random skus until the locations are some percentage full
"""
class PrepopulateLocations:
	def start(self,skus,locations,percentFill):
		"""
		type skus: Dictionary[string : Dictionary[string : float]]
		type locations: Dictionary[char : List[string]]
		type percentFill: float
		rtype: Dictionary[string : List[string]]
		TODO: check if locations are passed by reference
		"""
		
		index = locations["index"]
		locationsPer = len(locations[index[0]])
		totalLocations = len(index)*locationsPer
		numOfSkus = len(skus)
		
		if numOfSkus < totalLocations:
			#self.fillByMultipleSkus
		else:
			#self.fillBySingleSku(skus,locations,index,locationsPer)
