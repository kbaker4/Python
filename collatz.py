
def collatz(number):
	if number % 2 == 0:
		print(number // 2)
		return number // 2
	else:
		print(3 * number + 1)
		return 3 * number + 1

while True:
	print ("Enter a number or 'quit'")
	userInput = input()
	if userInput == 'quit':
		break
	else:
		try:
			number = int(userInput)
			while(number != 1):
				number = collatz(number)
		except:
			print("\nNot a valid choice\n")