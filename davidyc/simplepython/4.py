def bank(dep, year):
	while(year>0):
		proc = dep * 0.1
		dep += proc
		year -= 1
	return dep
	
print(bank(1000,5))