#Assignment Operators
a = 10
print("Initial value:", a)

a += 5      # a = 10 + 5 = 15
print("After += :", a)

a -= 3      # 15 - 3 = 12
print("After -= :", a)

a *= 2      # 12 * 2 = 24
print("After *= :", a)

a /= 4      # 24 / 4 = 6.0
print("After /= :", a)

a %= 4      # 6 % 4 = 2
print("After %= :", a)

a //= 2     # 2 // 2 = 1
print("After //= :", a)

a **= 3     # 1 ** 3 = 1
print("After **= :", a)

# Logical Operators
#1.AND
a = 10
print(a > 5 and a < 20)
#2. OR
a = 10
print(a > 5 or a > 20)
#3. NOT
a = 10
print(not(a > 5))

#Relational Operators
a = 10
b = 5

print("a == b :", a == b)   # Equal
print("a != b :", a != b)   # Not equal
print("a > b  :", a > b)    # Greater than
print("a < b  :", a < b)    # Less than
print("a >= b :", a >= b)   # Greater or equal
print("a <= b :", a <= b)   # Less or equal

#Membership Operators
text = "python"
nums = [1, 2, 3, 4]

print("p" in text)       # True
print("z" in text)       # False
print("y" not in text)   # False

print(2 in nums)         # True
print(5 not in nums)     # True

#Identity Operators
x = 10
y = 10
z = 20

print(x is y)        # True
print(x is z)        # False
print(x is not z)    # True

