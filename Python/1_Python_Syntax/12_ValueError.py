# Python automatically assigns a variable the appropriate datatype based on the value it is given. A variable with the value 7 is an integer, 7. is a float, "7" is a string. Sometimes we will want to convert variables to different datatypes. For example, if we wanted to print out an integer as part of a string, we would want to convert that integer to a string first. We can do that using str():
age = 13
print "I am " + str(age) + " years old!"

# Similarly, if we have a string like "7" and we want to perform arithmetic operations on it, we must convert it to a numeric datatype. We can do this using int()

number1 = "100"
number2 = "10"

string_addition = number1 + number2 
#string_addition now has a value of "10010"

int_addition = int(number1) + int(number2)
#int_addition has a value of 110

#If you use int() on a floating point number, it will round the number down. To preserve the decimal, you can use float()

string_num = "7.5"
print int(string_num)
print float(string_num)

# PROBLEM: Create a variable called product that contains the result of multiplying the float value of float_1 and float_2. Create a string called big_string that says: The product was X with the value of product where the X is

float_1 = 0.25
float_2 = 40.0
product = float_1 * float_2
big_string = "The product was " + str(product)
print big_string