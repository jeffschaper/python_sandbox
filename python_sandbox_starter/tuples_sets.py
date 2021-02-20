# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 #! ordered
 #* unchangable
 #! Allows duplcates

#! Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
#! Constructor
fruits2 = tuple(('Apples,' 'Oranges', 'Grapes'))

#* Single values needs a trailing comma
#* If a trailing comma is missing, python will interpret this as a string
fruits3 = ('Apples',)

#! Get value
print(fruits[1])
print('')

#! Can't change value
#* This will result in an type error
# fruits[0] = 'Pears'

#! Delete tuple
#* This will result in an error since fruits2 no longer exists
del fruits2
# print(fruits2)

#! Get length
print(len(fruits))
print('')

#? That's all for tuples! Biggest thing to remember is that tuples are unchangable


print('sets')
print('')
# A Set is a collection which is unordered and unindexed. No duplicate members.
#* unordered
#* unindexed
#* No duplicates

#! Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

#! Check if in set
print('Check if in set')
isIn = 'Apples' in fruits_set 
print(f'Return type {isIn}')
print('Apples' in fruits_set)
print('')

#! Add to set
#* It seems like add just adds the value at random
print('Add to set')
print(fruits_set)
fruits_set.add('Grape')
print(fruits_set)
print('')

#! Remove from set
print('Remove from set')
fruits_set.remove('Grape')
print(fruits_set)
print('')

#! Clear set
print('Clear set')
fruits_set.clear()
print(fruits_set)
print('')

#! Delete
print('Delete')
del fruits_set
#* This will result in an error
# print(fruits_set)