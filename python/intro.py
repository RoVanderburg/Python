print("""
     +-------------------------------------------------------+
     +                                                       +
     +                      PUSSY WIZARD                     +
     +                                                       +
     +-------------------------------------------------------+
""")

print('Welcome friend.')
print('')
name = input('What is your name?\n')
print("\n" + str(name) + ", you awake in a strange place, in a strange bed.  The room is small and smells faintly like stale smoke. There are clothes strewn about the floor and second hand art hanging on the walls.")
x = input('what would you like to do?\n')
x = x.lower()


if (x == 'get out of bed'):
	print('\n' + str(name) + ' you\'re out of bed. Now what?')
elif (x =='do nothing'):
	print('case2')
elif ( x =='quit'):
	print('Goodbye')
else:
	print('case3')