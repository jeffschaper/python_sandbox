# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1           # int
y = 2.5         # float
name = 'John'   # str (Can be single or double quotes)
is_cool = True  # bool (Must be capital T or capital F)

# print(is_cool)

#! Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)

# print(x, y, name, is_cool)

#! Basic Math
a = x + y

# print(a)

#! Casting
x = str(x)
y = int(y)
z = float(y)

#* Looks like you *can* cast to a bool, but it doesn't make sense in this case
xx = bool(x)

print(type(xx), xx)