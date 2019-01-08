def season(numberseason):
	if numberseason >= 1 and numberseason <= 2 or numberseason >= 12:
		return "зима"
	elif numberseason >= 3 and numberseason <= 5:
		return "весна"
	elif numberseason >= 6 and numberseason <= 8:
		return "лето"
	elif numberseason >= 9 and numberseason <= 11:
		return "осень"
		
		
for i in range(1,13):
	print(season(i) , str(i))