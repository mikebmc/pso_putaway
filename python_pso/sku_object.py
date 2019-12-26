"""
this is the sku object to be used throughout
"""

class PsoSku:
	def __init__(self,sku_name,max_associated=10):
		self.name = sku_name
		self.associated_skus = {}
		self.associated_count = 0
		self.associated_capacity = max_associated
		self.storage_locations = set()

	def store_in_location(self,location):
		self.storage_locations.add(location)

	def remove_from_location(self,location):
		try:
			self.storage_locations.remove(location)
		except:
			raise self.name + ' is not stored at ' + location

	def add_associated_sku(self,a_sku,a_strength):
		if a_strength > 1:
			raise 'associated strength cannot be greater than 1'
		if a_sku == self.name:
			raise 'sku cannot be associated to itself'
		self.associated_skus[a_sku] = a_strength
		self.associated_count = self.associated_count+1
		if self.associated_count > self.associated_capacity:
			self._remove_least_associated()

	def remove_associated_sku(self,a_sku):
		try:
			del self.associated_skus[a_sku]
		except:
			print("key not present in associated_skus")

	def _remove_least_associated(self):
		if len(self.associated_skus) == 0:
			if self.associayed_count > 0:
				self.associated_count = 0
			return

		min_val = 1
		min_key = ""
		for s,a in self.associated_skus.items():
			if self.associated_skus[s] < min_val:
				min_val = self.associated_skus[s]
				min_key = s
		self.remove_associated_sku(min_key)

