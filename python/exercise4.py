num = int(input("Enter a number"))
divisors = []

i = 1

while i < num:
	if num % i == 0:
		divisors.append(i)
	i += 1

print(divisors)