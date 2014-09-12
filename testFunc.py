#grabs user input and stores it in a local variable
def getValue():
	value = raw_input("Enter an integer > ")
	return value

#validates a local variable and returns it as an int if possible
#if variable cannot be returned as an int the program stops and
#tells the user they must run the program again and enter valid
#inputs
def validateValue(value):
	try:
		x = int(value)
		return int(x)
	except:
		print "Invalid input, run program again"
		exit()

#returns the area using variables for length and width		
def findArea(var1, var2):
	return var1 * var2
