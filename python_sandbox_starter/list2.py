#! Sorting appears to be alphabetical

techList = ['Apple','Microsoft','Facebook','Google','Amazon']

# print initial index
print(techList.index('Apple'),techList.index('Microsoft'),techList.index('Facebook'),techList.index('Google'),techList.index('Amazon'))
print(techList)

# sort list
techList.sort()
print(techList)

# reverse sort
techList.sort(reverse=True)
print(techList)