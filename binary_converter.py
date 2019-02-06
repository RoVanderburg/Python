#binary to decimal converter
import math
from math import log
import os

os.system('cls')

#declarations
s = True
v = True
def logb2(usimp):
	div = int(math.log(usimp,2))
	return div

def exit(val):
		val = False
		print('now exiting..')
		return

print ("""
	=-=-=-=-=-=-=-=-=-=-=-=-=
	 Python Binary Converter
	=-=-=-=-=-=-=-=-=-=-=-=-=
	 + type end to exit   +
	 + binary strings     +
	 + are 4 bits in      +
	 + lenth up to max of +
	 + 16 bits (4 bytes)  +   
		 """)

while s == True:
	v = True
	path = str(input('please choose which direction to convert\n(b: binary to decimal, d: decimal to binary)\n> '))

	while v == True:
		
		#begin binary path
		if path == 'b':

			total_out = 0
			handler = input('please enter binary string: ')

			
			if handler == 'end':
				exit(v)
				break

			num = list(handler)
			num.reverse()
			num_len = len(num)

			#verifies binary string integrity
			for number in num:
				number = int(number)
				if number != 0 and number != 1:
					print('invalid sequence, please enter only 1\'s and 0\'s')
					break

			#verifies inputs as bits/bytes
			if (num_len < 3) or (num_len > 16) or (num_len > 4 and num_len < 8) or (num_len > 8 and num_len < 16):
				print('\n4 byte (16 bit) maximum, please enter 4, 8 or 16 bit strings\n')
				continue

			#arithmetic operations
			for number in range(num_len):
				pham = int(num[number])
				if pham == 1:
					total_out = total_out + (2**number)
				else:
					continue
			print('\ndecimal output is: ' + str(total_out) + '\n')

		#exit path
		elif path == 'end':
			s = False
			break

		#begin decimal branch
		elif path == 'd':
			d = True
			total_out = []
			binary_out = []
			userin = input('please enter a whole integer number (1-255)\n> ')
			
			if userin == 'end':
				exit(v)
				break

			while d == True:
				userin = int(userin)
				if userin >=1:
					imp = logb2(userin)
					total_out.append(imp)
					userin = userin - 2**imp
				else:
					d = False

			for i in range((total_out[0])+1):
				binary_out.append(0)

			for i in total_out:
				binary_out[i-1] = 1	
			
			print('> binary output: ' + ''.join(str(t) for t in binary_out))
		else:
			v = False
			print('> unrecognized command please re-enter')
			
