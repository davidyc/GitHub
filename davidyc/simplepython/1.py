def is_year(year):
	if year % 4 == 0 :
		return True
	else:
		return False

print(is_year(2095));
print(is_year(2005));
print(is_year(2000));
