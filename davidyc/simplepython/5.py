def is_prime(num):
	if num < 1 or num > 1001 :
		print("error number")
		return False
	else:
		if num % 2 == 0:
			return False
		i = 2
		while(i<num):
			if num % i == 0:
				return False
			i += 1
		return True

print(is_prime(127))
print(is_prime(333))

			