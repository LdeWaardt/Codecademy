# Changing the contents of a variable is one of the essential operations. As the flow of a program progresses, data should be updated to reflect changes that have happened

# Updating a variable by adding or subtracting a number to the original contents of the variable has its own shorthand to make it faster and easier to read.

# We're trying to figure out how much it rained in the past year! Update the annual_rainfall variable to include the values from September to December.

january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06
september_to_december_rainfall = 5.16 + 7.20 + 5.06 + 4.06
annual_rainfall += september_to_december_rainfall
print annual_rainfall
