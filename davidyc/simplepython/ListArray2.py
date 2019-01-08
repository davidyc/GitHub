def ChetNeChet(list):
	chet = []
	unchet = []
	for item in list:
		if item % 2 == 0:
			chet.append(item)
		else:
			unchet.append(item)
	print(chet, end=' ')
	print(unchet, end=' ')
	
	
list = (1,2,3,4,5,6,7,8,9,10)
ChetNeChet(list)