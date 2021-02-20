# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#! unordered
#! changeable
#! indexed
#! no duplicates

#! Create dict
#* key:value pairs
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

#! Constructor
person3 = dict(first_name='Sara', last_name='Williams')

#! Get value
print('Get value')
#? ugh, I don't like the bracket method, javascript dot method is more elegant
print('Get first name')
print(person['first_name'])
print('Get last name')
print(person.get('last_name'))
print('')

#! add key/value
print('Add key/value pair')
person['phone'] = '555-555-5555'
print(person)
print('')

#! Get dict keys
print('Get dict keys')
print(person.keys())

#! Get dict values
print('Get dict values')
print(person.values())
print('')

#! copy dict
#* copies structure and data
print('Copy dict person 2')
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)
print('')

#! Remove item
print('Remove item from person dict')
del(person['age'])
person.pop('phone')
print(person)
print('')

#! Clear
print('Clear')
person.clear()
print(person)
print('')

#! Get length
#* Gets number of key:value pairs
print('Get length')
print(len(person2))
print('')

#! list of dict
print('list of dictionaries')
people = [
    {
        'name': 'Martha',
        'age': 30
    },
    {
        'name': 'Kevin', 
        'age': 25
    }
]
print(people)
print('Get speicific element from list dict')
print(people[1]['name'])
print(people[0].get('name'))
print('')