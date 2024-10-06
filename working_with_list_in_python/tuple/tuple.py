# tuples are immutable, so we cannot change the value of an element
fruits = ('apple', 'orange', 'lemon',)
print(fruits) # 'apple', 'orange', 'lemon'

letters = tuple("Python")
print(letters) # 'P', 'y', 't', 'h', 'o', 'n'

print(letters[-1])  # n

# tuples are ordered and can be nested
nested_tuple = (1, 2, 3, ('a', 'b', 'c'))
print(nested_tuple)  # (1, 2, 3, ('d', 'e', 'f'))

# tuples can be unpacked
for i in nested_tuple:
    print(f"{i} {nested_tuple}")