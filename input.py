# #PYTHON INPUTS

#user input refers to any information provided
#by the user to the program. User input is typically obtained through
#input mechanisms provided by the language.
#In python, the input() function is used to get user input.

first_name= input("Enter your first name: ")[0]
last_name= input("Enter your last name: ")[0]

print("My name is:", first_name, last_name)

# The default input type is string.

x= input("Enter a number: ")
y= input("Enter another number: ")

print(type(x))
print(type(y))

print("Adding, x and y will give me",int(x)+int(y))

#Exampl 2
a= int(input("Enter a number: "))
b= int(input("Enter another number: "))



# print("Adding, a and b will give me", a+b)

# if you want to input a float, you can use the float() function

ate_apples = bool(int(input("Did he eat an apple today?(1 for True and 0 for false): ")))

if ate_apples:
    print('Good boy you get a treat ')
    
demo= input("Do you support Tuesdays Demos(y/n): ")

if demo == 'y':
    print('Good job')
else:
    print('You are missing out')

