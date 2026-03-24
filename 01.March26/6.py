"""
PYTHON STRINGS & METHODS

- Strings are immutable → any modification creates a new object
- Indexing starts from 0, supports negative indexing
- Slicing: [start:end:step] (end is exclusive)
- Strings are iterable → can loop through characters
- 'find()' returns -1 if not found, 'index()' throws error
- '==' compares value, 'is' compares identity (same as general rule)
- Strings are Unicode by default in Python
- Common interview traps:
  • Modifying string directly → not allowed
  • Using '+' in loop → inefficient (use join)
  • strip() removes only leading/trailing spaces, not middle
"""

# ------------------ Creating Strings ------------------
name = "Harry"
city = 'Delhi'


# ------------------ Multiline Strings ------------------
message = """This is a
multi line
string"""


# ------------------ Indexing ------------------
text = "Python"

print(text[0])   # P
print(text[3])   # h
print(text[-1])  # n (last character)


# ------------------ Length ------------------
print(len(text))


# ------------------ Slicing ------------------
print(text[0:3])   # Pyt
print(text[2:])    # thon
print(text[:4])    # Pyth
print(text[-3:])   # hon
print(text[-5:-2]) # tho

# step
print(text[::2])   # Pto


# ------------------ Common Methods ------------------
text = "  Hello World  "

print(text.lower())
print(text.upper())
print(text.strip())   # removes leading/trailing spaces
print(text.replace("World", "Python"))

# split & join (important for interviews)
data = "apple,banana,orange"
items = data.split(",")

joined = ",".join(items)
print(joined)


# ------------------ Search ------------------
text = "Hello World"

print(text.find("World"))   # index or -1
# print(text.index("World"))  # same but raises error if not found


# ------------------ Start / End Check ------------------
email = "test@gmail.com"

print(email.startswith("test"))
print(email.endswith(".com"))


# ------------------ Concatenation ------------------
first = "Hello"
second = "World"

result = first + " " + second
print(result)


# ------------------ String Formatting ------------------
name = "Harry"
age = 25

msg = f"My name is {name} and I am {age} years old"
print(msg)


# ------------------ Checking Content ------------------
text = "Python123"

print(text.isalpha())   # only letters
print(text.isdigit())   # only numbers
print(text.isalnum())   # letters + numbers


# ------------------ Immutability ------------------
text = "Python"

# text[0] = "J"  # ❌ Error (strings are immutable)

# correct way
new_text = "J" + text[1:]
print(new_text)