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
