"""
PYTHON LISTS & METHODS - QUICK NOTES (INTERVIEW READY)

- Lists are mutable → can modify after creation
- Can store mixed data types
- Indexing: 0-based, supports negative indexing
- Slicing: [start:end:step]
- Important:
  • append() → adds single element
  • extend() → adds multiple elements
  • insert() → adds at index
- pop() returns removed element
- remove() removes by value (first occurrence)
- sort() modifies list, sorted() returns new list
- copy() → shallow copy (watch for nested lists)
"""

# ------------------ Creating Lists ------------------
numbers = [1, 2, 3, 4]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "Python", 3.5, True]


# ------------------ Indexing ------------------
items = ["apple", "banana", "orange"]

print(items[0])   # apple
print(items[2])   # orange
print(items[-1])  # orange


# ------------------ Length ------------------
print(len(items))  # 3


# ------------------ Slicing ------------------
items = ["apple", "banana", "orange", "mango"]

print(items[1:3])  # ['banana', 'orange']
print(items[:2])   # ['apple', 'banana']
print(items[2:])   # ['orange', 'mango']


# ------------------ Modify ------------------
items = ["apple", "banana", "orange"]
items[1] = "grapes"

print(items)  # ['apple', 'grapes', 'orange']


# ------------------ Add Elements ------------------
items = ["apple", "banana"]

items.append("orange")
print(items)  # ['apple', 'banana', 'orange']

items.insert(1, "grapes")
print(items)  # ['apple', 'grapes', 'banana', 'orange']

items.extend(["mango", "pineapple"])
print(items)  # ['apple', 'grapes', 'banana', 'orange', 'mango', 'pineapple']


# ------------------ Remove Elements ------------------
items = ["apple", "banana", "orange"]

items.remove("banana")
print(items)  # ['apple', 'orange']

items.pop()
print(items)  # ['apple']

items = ["apple", "banana", "orange"]
removed = items.pop(0)
print(removed)  # apple
print(items)    # ['banana', 'orange']

items.clear()
print(items)  # []


# ------------------ Search ------------------
items = ["apple", "banana", "apple"]

print(items.index("banana"))  # 1
print(items.count("apple"))   # 2


# ------------------ Sorting ------------------
numbers = [3, 1, 4, 2]

numbers.sort()
print(numbers)  # [1, 2, 3, 4]

numbers.sort(reverse=True)
print(numbers)  # [4, 3, 2, 1]

nums = [3, 1, 4, 2]
new_list = sorted(nums)
print(new_list)  # [1, 2, 3, 4]
print(nums)      # [3, 1, 4, 2] (unchanged)


# ------------------ Reverse ------------------
items = ["apple", "banana", "orange"]

items.reverse()
print(items)  # ['orange', 'banana', 'apple']


# ------------------ Copy ------------------
items = ["apple", "banana"]
new_items = items.copy()

print(new_items)  # ['apple', 'banana']


# ------------------ Membership ------------------
items = ["apple", "banana", "orange"]

print("apple" in items)  # True
print("grapes" in items) # False


# ------------------ Practice Snippets ------------------
names = ["Harry","Larry", "Perry", "Rohan"]
elements = [1, 34, 67, False, True]

print(elements[1:4])  # [34, 67, False]
print(len(elements))  # 5

elements[2] = 69
print(elements)  # [1, 34, 69, False, True]


items = ["apple", "banana", "orange"]
print(items)  # ['apple', 'banana', 'orange']


numbers = [11, 1, 4, 5, 55, 78, 2, 9]
numbers.sort(reverse=True)
print(numbers)  # [78, 55, 11, 9, 5, 4, 2, 1]

print(11 in numbers)  # True