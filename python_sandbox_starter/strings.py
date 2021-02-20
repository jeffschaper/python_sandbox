# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

#! Concatenate
#* Will error is age is not cast to a string
print('Hello, my name is ' + name + ' and I am ' + str(age))

#! String Formatting

#! Arguments by position
#* .format() method
#* {name} = Brad
#* {age} = 37
print('My name is {name} and I am {age}'.format(name=name, age=age))

#! F-Strings (Python 3.6 or later)
#* This is the preferred way
print(f'Hello, my name is {name} and I am {age}')


#! String Methods
#* There are several others not mentioned here

# Examples
s = 'hello world'
#s = 'Jeff is cool!'
print(' ')
print(f'Original string is {s}')
print(' ')

#! Capitalize string
print('capitalize')
print(f'Return type {type(s.capitalize())}')
print(s.capitalize())
print(' ')

#! Make all uppercase
print('uppercase')
print(f'Return type {type(s.upper())}')
print(s.upper())
print(' ')

#! Make all lower
print('lowercase')
print(f'Return type {type(s.lower())}')
print(s.lower())
print(' ')

#! Swap case
print('swapcase')
print(f'Return type {type(s.swapcase())}')
print(s.swapcase())
print(' ')

#! Get length
print('length')
print(f'Return type {type(len(s))}')
print(len(s))
print(' ')

#! Replace
print('replace')
replaceType = type(s.replace('world', 'everyone'))
print(f'Return type {replaceType}')
print(s.replace('world', 'everyone'))
print(' ')

#! Count
print('count')
sub = 'h'
print(f'Return type {type(s.count(sub))}')
print(s.count(sub))
print('')

#! Starts with
print('starts with')
Stype = type(s.startswith('hello'))
print('Return type {returnType}'.format(returnType=Stype))
print(s.startswith('hello'))
print('')

#! Ends with
print('ends with')
print(f'Return type {type(s.endswith("d"))}')
print(s.endswith('d'))
print('')

#! Split into a list
print('split')
print(f'Return type {type(s.split())}')
#* Lists are the same as arrays in other languages
print(s.split())
print('')

#! Find position
print('find position')
pType = type(s.find('r'))
print(f'Return type {pType}')
print(s.find('r'))
print('')

#! Is all alphanumeric
print('alphanumeric')
#* Returns False in this case because of the space
print(f'Return type {type(s.isalnum())}')
print(s.isalnum())
print('')

#! Is all alphabetic
print('alphabetic')
print(f'Return type {type(s.isalpha())}')
#* Returns False in this case because of the space
print(s.isalpha())
print('')

#! Is all numeric
print('numberic')
print(f'Return type {type(s.isnumeric())}')
#* Returns False in this case because of the space
print(s.isnumeric())
print('')