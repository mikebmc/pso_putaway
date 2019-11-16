"""
the goal of this module is to take a list of skus and
a set of locations, and to populate the locations with
random skus until the locations are some percentage full
"""

class PrepopulateLocations:
	def start(self,skus,locations):
		"""
		type skus: Dictionary[string : Dictionary[string : float]]
		type locations: Dictionary[char : List[string]]
		rtype: tbd
		"""