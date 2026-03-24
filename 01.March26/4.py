#The input() Function pauses the program and waits for the user to type something. Whatever the user types is stored in the variable name.

name = input()


#Taking Input with a Prompt Message , You can guide the user by showing a message inside input().

name = input("Enter your name: ")


# By default, all input taken using input() is a string. Even if the user enters a number, Python will treat it as text.

age = input("Enter your age: ")
type(age)

# The data type of age will be str. If you want to perform calculations, you must convert the input.

age = int(input("Enter your age: "))
price = float(input("Enter product price: "))

quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
 
total = quantity * price
print("Total amount:", total)

# Common Input Errors If the user enters invalid data, the program will crash.

age = int(input("Enter age: "))

# If the user types text instead of a number, an error will occur.
