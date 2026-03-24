# Comments in Python, Comments are written for humans, not for Python, it completely ignores comments while running the code.
#What is Type Conversion? Type conversion means changing one data type into another.

age = "25"
age = int(age)

price = "1999.99"
price = float(price)

total = 500
message = "Total sales: " + str(total)

#Common Errors in Type Conversion Not every string can be converted into a number.
value = "abc"
int(value)
#This will cause an error.
