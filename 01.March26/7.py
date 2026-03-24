"""
PYTHON F-STRINGS

- Syntax: f"{variable}"
- Supports expressions, method calls, formatting
- Faster & more readable than '+' and .format()

Important:
- f"{2+3}" → '5'
- f"{name.upper()}" → method inside
- Use for clean code in interviews

Common Mistake:
- Forgetting 'f' → no interpolation happens
"""

# ------------------ Basic Example ------------------
name = "Harry"
age = 25

print(f"My name is {name} and I am {age} years old")
# Output: My name is Harry and I am 25 years old


# ------------------ Expression ------------------
a = 5
b = 3

print(f"Sum: {a + b}")
# Output: Sum: 8


# ------------------ Method Call ------------------
name = "harry"

print(f"Upper: {name.upper()}")
# Output: Upper: HARRY


# ------------------ Formatting ------------------
pi = 3.14159

print(f"{pi:.2f}")
# Output: 3.14


# ------------------ Input Example ------------------
name = "Harry"
work = "CodeWithHarry"
live = "Delhi"

print(f"{name} works at {work} and lives in {live}")
# Output: Harry works at CodeWithHarry and lives in Delhi


# ------------------ Old vs New ------------------
# Old (avoid)
# print(name + " works at " + work)

# New (recommended)
# print(f"{name} works at {work}")