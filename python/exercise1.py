# Ask user for name and age
# Determine the year the user will turn 100
import datetime

name = input("What is your name?\n")
age = int(input("How old are you?\n"))


newage = 100 - age

date = datetime.datetime.now()

hundred = date.year + newage

print("\n" + str(name) + " you will be 100 years old in the year " + str(hundred))
