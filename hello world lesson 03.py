#program says hello and asks for a name
print('hello world') #print(' is a call to function')
print('what is your name?')

#ask user for a name
myName = input() #expression
print('it is good to meet you, ' + myName)
print('the length of your name is:')
print(len(myName))

#ask user for an age
print('what is your age?')
myAge = input()
print('you will be ' + str(int(myAge) + 1 ) + ' in a year')

#quit
input('Press enter to quit')
