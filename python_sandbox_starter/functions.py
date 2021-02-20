# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
#? I kind of like the curly braces

#! Create function
'''
    This function's purpose in life is to say hello to anyone who asks
    this is just the definition of the function, it needs to be called in order to run the code
'''
#* if a name parameter is not provided, default to 'superstar'
def sayHello(name = 'superstar'):
    print(f'Hello, {name}!')

sayHello()

#! Retrun values
# def getSum(num1, num2):
#     total = num1 + num2
#     return total

# num = getSum(3,4)
# print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
#? pass parameters on variable
print(getSum(10, 3))