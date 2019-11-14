class GenerateSkus:
	def permutateSkus(numOfSkus):
		"""
		:type numOfSkus: int
		:rtype: List[string]
		"""
		skus = []
		letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		numbers = [0,1,2,3,4,5,6,7,8,9]
		permutateHelper(skus,numOfSkus,letters,numbers,[])
		return skus
		
	def permutateHelper(skus,numOfSkus,letters,numbers,perm):
		if len(skus) == numOfSkus:
					return
		if len(perm) == 6:
			skus.append(perm[:])
			return
		else:
			if len(perm) == 2 and lnp < len(numbers):
				for i in range(len(numbers)):
					perm.append(numbers[i])
					permutateHelper(skus,numOfSkus,letters,numbers,perm)
					perm.pop()
			elif len(perm) == 5 and rnp < len(numbers):
				for i in range(len(numbers)):
					perm.append(numbers[i])
					permutateHelper(skus,numOfSkus,letters,numbers,perm)
					perm.pop()
			else:
				for i in range(len(letters)):
					perm.append(letters[i])
					permutateHelper(skus,numOfSkus,letters,numbers,perm)
					perm.pop()
