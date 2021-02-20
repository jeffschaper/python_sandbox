# A variable is a container for a value, which can be of various types
#! Comments
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

#! Assignment
x = 1           # int
y = 2.5         # float
name = 'John'   # str (Can be single or double quotes)
is_cool = True  # bool (Must be capital T or capital F)

print('x = {x} '.format(x=x))
print('y = {y} '.format(y=y))
print('name = {name} '.format(name=name))
print('Is Jeff Cool? {is_cool}'.format(is_cool=is_cool))
print(' ')

#! Multiple assignment
x, y, name, is_cool = (1, 2.5, 'John', True)
print('print multiple variables')
print(x, y, name, is_cool)
print(' ')

#! Basic Math
print('print basic math')
a = x + y
print(f'x + y = {a}')
print(' ')

#! Casting
print('casting')
x = str(x)
print(x)
print(f'x is now {type(x)}')
print(' ')

y = int(y)
print(y)
print(f'y is now {type(y)}')
print(' ')

z = float(y)
print(z)
print(f'z is now {type(z)}')
print(' ')

#* Notice how z here is different then y on line 18.
#* This is because a float was cast to an int then back to a float and cannot retain it's original value of 2.5
print(y)

#* Looks like you *can* cast to a bool, but it doesn't make sense in this case
xx = bool(x)

print(type(xx), xx)