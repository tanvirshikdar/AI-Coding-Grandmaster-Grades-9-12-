def powerOf8(number):
	
	bitPosition = 0
	mask = 1
	
	while (bitPosition <= 63):
		mask <<= bitPosition

		if (mask == number):
			return True

		bitPosition += 3
		mask = 1

	return False

number = int(input("Enter your number : "))
if (powerOf8(number)):
	print("Yes ",number,"is power of 8")
else:
	print("No ",number,"is not power of 8")