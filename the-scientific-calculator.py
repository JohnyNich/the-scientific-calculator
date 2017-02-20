import math
import time
import sys
operations = ["power", "equation"]
def word_by_word(sentence):
	for letter in sentence:
		print(letter, end="")
		sys.stdout.flush()
		time.sleep(0.1)
	print ("")
def power(num, power):
	return int(num)**int(power)
print (power(4, 5))
word_by_word("Welcome to the scientific calculator!")
while True:
	word_by_word("Enter an operation. To view operations, type operations. To exit this program, enter quit")
	operation = input("")
	if operation == "operations":
		word_by_word(operations)
	elif operation == "power":
		word_by_word("What is the numnber you want to power?")
		to_power = input("")
		word_by_word("To what power?")
		power_to_power = input("")
		word_by_word(to_power + " to the power of " + power_to_power + " is " + str(power(to_power, power_to_power)))
		
