a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = []

user = int(input("Enter a number\n"))

for num in a:
	if num < user:
		new.append(num)

print(new)