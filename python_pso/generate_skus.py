import random

class GenerateSkus:
	def permutateSkus(self,numOfSkus):
		"""
		:type numOfSkus: int
		:rtype: List[string]
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
			associatedDict = {}
			sku = skus[i]
			while len(associatedDict) < numOfAssociated:
				randSku = skus[random.randint(0,numOfSkus-1)]
				if randSku not in associatedDict and randSku != sku:
					associatedDict[randSku] = round(random.random(),3)
			skuDict[sku] = associatedDict
		return skuDict
