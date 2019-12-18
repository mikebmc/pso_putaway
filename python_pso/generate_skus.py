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
			raise "import hack failed"
			
# ImportHack()

import random
from sku_object import PsoSku

class GenerateSkus:
	def permutateSkus(self,numOfSkus):
		"""
		:type numOfSkus: int
		:rtype: Dictionary[string : Dictionary[string : float]] 
		"""
		skus = []
		letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		numbers = [0,1,2,3,4,5,6,7,8,9]
		self.permutateHelper(skus,numOfSkus,letters,numbers,[])
		return skus

	def permutateHelper(self,skus,numOfSkus,letters,numbers,perm):
		if len(skus) == numOfSkus:
					return
		if len(perm) == 6:
			skus.append(''.join(perm[:]))
			return
		else:
			if len(perm) == 2:
				for i in range(len(numbers)):
					perm.append(str(numbers[i]))
					self.permutateHelper(skus,numOfSkus,letters,numbers,perm)
					perm.pop()
			elif len(perm) == 5:
				for i in range(len(numbers)):
					perm.append(str(numbers[i]))
					self.permutateHelper(skus,numOfSkus,letters,numbers,perm)
					perm.pop()
			else:
				for i in range(len(letters)):
					perm.append(letters[i])
					self.permutateHelper(skus,numOfSkus,letters,numbers,perm)
					perm.pop()

	def getSkus(self,numOfSkus,numOfAssociated):
		skuDict = {}
		skus = self.permutateSkus(numOfSkus)
		for i in range(numOfSkus):
			sku = PsoSku(skus[i],numOfAssociated)
			while len(sku.associated_skus) < numOfAssociated:
				randSku = skus[random.randint(0,numOfSkus-1)]
				if randSku not in sku.associated_skus and randSku != sku:
					sku.associated_skus[randSku] = round(random.random(),3)
			skuDict[sku.name] = sku
		return skuDict
		
class TestSkuGeneration:
	skus = GenerateSkus().getSkus(5000,5)
	for sku in skus.values():
		print(sku.name, sku.associated_skus)
