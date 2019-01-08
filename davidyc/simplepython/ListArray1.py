import random

def ChetNeChet(list):
	chet = 0
	unchet = 0
	for item in list:
		if item % 2 == 0:
			chet += 1
		else:
			unchet += 1
	print("Четных", chet)
	print("Нечетные", unchet)
	
	
list = (1,2,3,4,5,6,7,8,9,10)
ChetNeChet(list)