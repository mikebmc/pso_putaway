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