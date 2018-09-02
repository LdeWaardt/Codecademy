# We have seen how to define a string with single quotes and with double quotes. If we want a string to span multiple lines, we can also use triple quotes. This address spans multiple lines, and is still contained in one variable, address_string. When a string like this is not assigned to a variable, it works as a multi-line comment. This can be helpful as your code gets more complex:

"""The following piece of code does the following steps:
takes in some input
does An Important Calculation
returns the modified input and a string that says "Success!" or "Failure..."
"""
... a complicated piece of code here...

# Create a variable called haiku and store this haiku as a multi-line string

haiku = """The old pond,
A frog jumps in:
Plop!"""

print haiku