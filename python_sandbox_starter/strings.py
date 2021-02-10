# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

#! Concatenate
#* Will error is age is not cast to a string
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

#! Arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

#! F-Strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

#! Capitalize string
#? Returns str
print(s.capitalize(), type(s.capitalize()))

#! Make all uppercase
#? Returns str
print(s.upper(), type(s.upper()))

#! Make all lower
#? Returns str
print(s.lower(), type(s.lower()))

#! Swap case
#? Returns str
print(s.swapcase(), type(s.swapcase()))

#! Get length
#? Returns int
print(len(s), type(len(s)))

#! Replace
#? Returns str
print(s.replace('world', 'everyone'), type(s.replace('world', 'everyone')))

#! Count
#? Returns int
sub = 'h'
print(s.count(sub), type(s.count(sub)))

#! Starts with
#? Returns bool
print(s.startswith('hello'), type(s.startswith('hello')))

#! Ends with
#? Returns bool
print(s.endswith('d'), type(s.endswith('d')))

#! Split into a list
#? Returns list
#* Lists are the same as arrays in other languages
print(s.split(), type(s.split()))

#! Find position
#? Returns int
print(s.find('r'), type(s.find('r')))

#! Is all alphanumeric
#? Returns bool
#* Returns False in this case because of the space
print(s.isalnum(), type(s.isalnum()))

#! Is all alphabetic
#? Returns bool
#* Returns False in this case because of the space
print(s.isalpha(), type(s.isalpha()))

#! Is all numeric
#? Returns bool
print(s.isnumeric(), type(s.isnumeric()))