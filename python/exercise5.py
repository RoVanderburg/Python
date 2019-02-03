from random import *

x = 11

a = []
b = []
same = []

i = 0

def tran(max):
	y = randint(1,max)
	return y

while i < x:
	a.append(tran(20))
	b.append(tran(20))
	i += 1

print(a)
print(b)

for numa in a:
	for numb in b:
		if numa == numb:
			same.append(numa)

print(same)