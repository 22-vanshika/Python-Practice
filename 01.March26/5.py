"""
- Operators are symbols used to perform operations on variables and values.
- Important distinction:
  • '/' → always returns float
  • '//' → floor division (integer result)
- 'is' vs '==':
  • '==' compares values
  • 'is' compares memory location (object identity)
- Short-circuit:
  • 'and' → stops if first is False
  • 'or' → stops if first is True
- Bitwise operators work at binary level (used in low-level optimization)
- Operator precedence matters → use parentheses for clarity
"""


# =========================
# ARITHMETIC OPERATORS
# =========================

a, b = 10, 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3
print(a % b)    # 1
print(a ** b)   # 1000


# =========================
# ASSIGNMENT OPERATORS
# =========================

x = 10
x += 5          # 15
x -= 2          # 13
x *= 2          # 26
x //= 3         # 8
x **= 2         # 64
print(x)        # 64


# =========================
# COMPARISON OPERATORS
# =========================

a, b = 10, 5

print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)   # False


# =========================
# LOGICAL OPERATORS
# =========================

a, b = 10, 3

print(a > 5 and b < 5)   # True
print(a > 5 or b > 10)   # True
print(not(a > 5))        # False


# =========================
# BITWISE OPERATORS
# =========================

a, b = 5, 3   # 5=101, 3=011

print(a & b)   # 1   (001)
print(a | b)   # 7   (111)
print(a ^ b)   # 6   (110)
print(~a)      # -6  (invert bits)
print(a << 1)  # 10  (shift left)
print(a >> 1)  # 2   (shift right)


# =========================
# MEMBERSHIP OPERATORS
# =========================

nums = [1, 2, 3]

print(2 in nums)        # True
print(5 not in nums)    # True


# =========================
# IDENTITY OPERATORS
# =========================

a = [1, 2]
b = a
c = [1, 2]

print(a is b)       # True   (same object)
print(a is c)       # False  (different object)
print(a == c)       # True   (same value)


# =========================
# OPERATOR PRECEDENCE
# =========================

print(2 + 3 * 4)        # 14   (* first)
print((2 + 3) * 4)      # 20   (parentheses first)

# Order:
# () > ** > * / // % > + - > comparisons > logical