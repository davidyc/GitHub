def Mysqrt(side):
	#периметр квадрата,
	pir = side * 4
	#площадь квадрата
	area = 	side ** 2
    #диагональ квадрата.
	dia = side ** 2 / 2
	cort = (pir, area, dia)
	return cort
	
new = Mysqrt(4)

print(new, end=' ')