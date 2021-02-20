# A List is a collection which is ordered and changeable. Allows duplicate members.
#? Ordered
#? What exactly does ordered mean?
    #* W3 Schools - When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
    #* If you add new items to a list, the new items will be placed at the end of the list.
#? Changeable
#? Allows Duplicate values
#* Similar to arrays in other languages


#! Create list
#* Just use square brackets; it's easier to identify
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#! Use a constructor
#? Double parentesis are intentional
numbers2 = list((1, 2, 3, 4, 5))

#! List Methods

#! Get a value at a particular index
print(f'{fruits[1]} is at index 1')
print(fruits[1])
print(' ')

#! Get length
print(f'the lenth of the fruits list is {len(fruits)}')
print(' ')

#! Append to list
Mango = 'Mangos'
print('append {newFruit} to the list'.format(newFruit=Mango))
fruits.append('Mangos')
print(fruits)
print(' ')

#! Remove from list
Grape = 'Grapes'
print('remove {fruit} from list'.format(fruit=Grape))
fruits.remove('Grapes')
print(fruits)
print(' ')

#! Remove with pop
print(f'pop {fruits[2]} from list')
fruits.pop(2)
print(fruits)
print(' ')

#! Insert into position
strawberry = 'Strawberries'
print('instert {strawberry} at index 2'.format(strawberry=strawberry))
fruits.insert(2, strawberry)
print(fruits)
print(' ')

#! Change value
change = 'Blueberries'
print(f'change {fruits[0]} to {change}')
fruits[0] = change
print(fruits)
print(' ')

#! Reverse list
print('reverse list')
fruits.reverse()
print(fruits.index('Blueberries'), fruits.index('Oranges'), fruits.index('Strawberries'), fruits.index('Mangos'))
print(fruits)
print(' ')


#* This section is a little confusing
#? is sort, sorting alphabetically or by index?
#! Sort list
print('sort the list')
fruits.sort()
print(fruits.index('Blueberries'), fruits.index('Mangos'), fruits.index('Oranges'), fruits.index('Strawberries'))
print(fruits)
print(' ')

#! Reverse sort
print('reverse sort the list')
fruits.sort(reverse=True)
print(fruits)
print(' ')