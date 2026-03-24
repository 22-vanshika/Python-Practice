"""
PYTHON TUPLES & METHODS

- Tuples are immutable → cannot modify after creation
- Faster than lists (used for fixed data)
- Can store mixed data types
- Indexing & slicing same as lists
- Only 2 methods: count(), index()

Important:
- Single element tuple → must use comma (5,)
- Tuple unpacking is common in interviews
- Can be used as dictionary keys (lists cannot)
"""

# ------------------ Creating Tuples ------------------
numbers = (1, 2, 3)
names = ("Alice", "Bob", "Charlie")
mixed = (1, "Python", 3.5, True)


# ------------------ Single Element ------------------
single = (5,)
print(type(single))  # <class 'tuple'>

not_tuple = (5)
print(type(not_tuple))  # <class 'int'>


# ------------------ Indexing ------------------
items = ("apple", "banana", "orange")

print(items[0])   # apple
print(items[2])   # orange
print(items[-1])  # orange


# ------------------ Length ------------------
print(len(items))  # 3


# ------------------ Slicing ------------------
items = ("apple", "banana", "orange", "mango")

print(items[1:3])  # ('banana', 'orange')
print(items[:2])   # ('apple', 'banana')
print(items[2:])   # ('orange', 'mango')


# ------------------ Immutability ------------------
items = ("apple", "banana", "orange")

# items[1] = "grapes"  # ❌ Error (immutable)


# ------------------ Methods ------------------
items = ("apple", "banana", "apple")

print(items.count("apple"))  # 2
print(items.index("banana")) # 1


# ------------------ Loop ------------------
items = ("apple", "banana", "orange")

for item in items:
    print(item)
# Output:
# apple
# banana
# orange


# ------------------ Packing & Unpacking ------------------
data = (10, 20, 30)

a, b, c = data
print(a, b, c)  # 10 20 30


# ------------------ Convert ------------------
items = ("apple", "banana")

list_1 = list(items)
print(list_1)  # ['apple', 'banana']

tuple_1 = tuple(list_1)
print(tuple_1)  # ('apple', 'banana')


# ------------------ Practice ------------------
numbers = (1, 4, 6)

print(numbers[0])  # 1
print(numbers[1])  # 4
print(numbers[2])  # 6