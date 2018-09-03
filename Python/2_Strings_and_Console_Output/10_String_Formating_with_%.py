# String Formatting with %, Part 1

# When you want to print a variable with a string, there is a better method than concatenating strings together.

name = "Mike"
print "Hello %s" % (name)

# The % operator after the string is used to combine a string with variables. The % operator will replace the %s in the string with the string variable that comes after it.

# If you'd like to print a variable that is an integer, you can "pad" it with zeros using %02d. The 0 means "pad with zeros", the 2 means to pad to 2 characters wide, and the d means the number is a signed integer (can be positive or negative).

day = 6
print "03 - %s - 2019" %  (day)
# 03 - 6 - 2019
print "03 - %02d - 2019" % (day)
# 03 - 06 - 2019

# PROBLEM: Take a look at the code in the editor. What do you think it'll do? Click Run when you think you know.

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

# Remember, we used the % operator to replace the %s placeholders with the variables in parentheses.

name = "Mike"
print "Hello %s" % (name)

#You need the same number of %s terms in a string as the number of variables in parentheses:

print "The %s who %s %s!" % ("Knights", "say", "Ni")
# This will print "The Knights who say Ni!"

# PROBLEM 2: Now it's your turn! We have ___ in the code to show you what you need to change! Inside the string, replace the three ___ with %s. After the string but before the three variables, replace the final ___ with a %. Hit Run.  Answer the questions in the console as they pop up! Type in your answer and hit Enter.

name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)