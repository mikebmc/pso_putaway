#this is needed to import on pythonista
import sys
import importlib

class ImportHack:
	def __init__(self, loc=None):
	# update or append instance
		for i, mp in enumerate(sys.meta_path):
			if mp.__class__.__name__ == 'ImportHack':
				sys.meta_path[i] = self
				return
			sys.meta_path.append(self)
	@staticmethod
	def find_spec(fullname, path, target):
		import_loc = __file__.rpartition('/')[0]
		module_loc = import_loc + '/' + fullname + '.py'
		try:
			# test if target exists in same location without use of additional imports
			f = open(module_loc)
			f.close()
			return importlib.util.spec_from_file_location(fullname, module_loc)
		except Exception:
			pass					
ImportHack()

# begin script
import random
from sku_object import PsoSku
from generate_skus import GenerateSkus

def getSkus(numOfSkus,numOfAssociated):
	skuDict = {}
	skus = GenerateSkus().permutateSkus(numOfSkus)
	for i in range(numOfSkus):
		sku = PsoSku(skus[i],numOfAssociated)
		while len(sku.associated_skus) < numOfAssociated:
			randSku = skus[random.randint(0,numOfSkus-1)]
			if randSku not in sku.associated_skus and randSku != sku:
				sku.associated_skus[randSku] = round(random.random(),3)
		skuDict[sku.name] = sku
	return skuDict
		
class PsoTests:
	def generateSkus(self):
		skus = getSkus(10,5)
		for sku in skus.values():
			print(sku.name, sku.associated_skus)

	def testSkus(self):
		tSku = PsoSku('AA0', 2)
		print(tSku.name, tSku.associated_capacity)
		print()
	
		print('adding associated skus')
		tSku.add_associated_sku('AA1',.9)
		tSku.add_associated_sku('AA2',.2)
		tSku.add_associated_sku('AA3',.7)
	
		print('printing skus')
		for i,j in tSku.associated_skus.items():
			print(i,j)
	
		print()
		print('removing sku=AA1')
		tSku.remove_associated_sku('AA1')
		for i,j in tSku.associated_skus.items():
			print(i,j)
	
		print()
		print('adding 3 storage locations')
		tSku.store_in_location('ST1')
		tSku.store_in_location('ST2')
		tSku.store_in_location('ST3')
		for i in tSku.storage_locations:
			print(i)
	
		print()
		print('removing storage_location=ST1')
		tSku.remove_from_location('ST1')
		for i in tSku.storage_locations:
			print(i)
	
		print()
		print('attempting to remove ST1 again')
		try:
			tSku.remove_from_location('ST1')
		except:
			print('exception caught while attempting to remove location=ST1')

PsoTests().generateSkus()
PsoTests().testSkus()
