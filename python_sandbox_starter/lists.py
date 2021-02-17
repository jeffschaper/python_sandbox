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

#! Get a value
print(fruits[1])

#! Get length
print(len(fruits))

#! Append to list
fruits.append('Mangos')
print(fruits)

#! Remove from list
fruits.remove('Grapes')
print(fruits)

#! Remove with pop
fruits.pop(2)
print(fruits)

#! Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

#! Change value
fruits[0] = 'Blueberries'
print(fruits)

#! Reverse list
fruits.reverse()
print(fruits)

#! Sort list
fruits.sort()
print(fruits)

#! Reverse sort
fruits.sort(reverse=True)
print(fruits)