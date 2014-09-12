#code I used to test the code written in testFunc.py
import testFunc

print "This program will find area"

#asks user for length then uses getValue() to grab user input
#uses validateValue(value) to make sure that the input provided
#is an integer and if not stops the program
print "Enter length"
length = testFunc.getValue()
var1 = testFunc.validateValue(length)

#asks user for width then uses getValue() to grab user input
#uses validateValue(value) to make sure that the input provided
#is an integer and if not stops the program
print "Enter width"
width = testFunc.getValue()
var2 = testFunc.validateValue(width)

#uses findArea(var1, var2) to print out the area of the validated
#inputs
area = testFunc.findArea(var1, var2)
print "Area is %d" % area
