#binary to decimal converter
import math

#declarations
s = True
while s == True:
	path = str(input('please choose which direction to convert\n(b: binary to decimal, d: decimal to binary)\n'))

	v = True
	while v == True:
		
		#begin binary path
		if path == 'b':

			d_total = 0
			temp = input('please enter binary string: ')

			if temp == 'end':
				v = False
				print('now exiting')
				break
			num = list(temp)
			num.reverse()
			num_len = len(num)

			#verifies binary string integrity
			for number in num:
				number = int(number)
				if number != 0 and number != 1:
					print('invalid sequence, please enter only 1\'s and 0\'s')
					break

			#verifies inputs as bits/bytes
			if num_len > 16:
				print('\n4 byte (16 bit) maximum, please enter 4, 8 or 16 bit strings\n')
				continue
			elif num_len > 4 and num_len < 8:
				print('\n4 byte (16 bit) maximum, please enter 4, 8 or 16 bit strings\n')
				continue
			elif num_len > 8 and num_len < 16:
				print('\n4 byte (16 bit) maximum, please enter 4, 8 or 16 bit strings\n')
				continue	
			elif num_len%2 != 0:
				print('\nbinary string is odd, please enter 4, 8 or 16 bit strings\n')

			#arithmetic operations
			for number in range(num_len):
				pham = int(num[number])
				if pham == 1:
					d_total = d_total + (2**number)
				else:
					continue
			print('\nbinary output is: ' + str(d_total) + '\n')

		#exit path
		elif path == 'end':
			s = False
			print('now exiting')			
			break

		#begin decimal path
		else:

			d_total = []
			temp = input('please enter decimal (whole integer) number (1-255)\n')
			num = int(temp)

			#end conditions
			if temp == 'end':
				('exiting')
				break

			baisc = []
			base_2 = []
			logger = 2

			while logger != 0:
				basic.append(int(math.log(num,2))

			deci = int(math.log(num,2))
			# div = math.log(temp,2)
			# div = int(div)
			# misc = temp - (2**div)
			# nex = math.log(misc,2)
			# nex = int(nex)
			# print(div)
			# print(nex)			


