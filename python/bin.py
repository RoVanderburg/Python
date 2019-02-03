#binary converter

path = input('please choose path of conversion (b: binary to decimal; d: decimal to binary): ')

total = 0

if path == 'b':
	temp = input('please enter binary string: ')
	num = list(temp)
	num.reverse()
	print(num)

	for number in range(len(num)):
		#print(number)
		pham = int(num[number])
		if pham == 1:
			total = total + (2**number)
		else:
			continue
	print(total)

else:
	num = input('please enter decimal string: ')
