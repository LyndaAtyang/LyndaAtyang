#DATA TYPES- SEQUENCES
"""This is a string
that spans across multiple lines
we use triple single quotes or triple double quotes"""

#1. Strings 
#Strings are sequences of characters, using the syntax of either
# single quotes or double quotes:

name = "John"
num = "123"
age = '45'
my_string = "Hello, World!"

#2. Multi-line strings
#Multi-line strings are strings that span across multiple lines.

#Typecasting to string

print(type(name)) #<class 'str'>
print(type(num)) #<class 'str'>


num = "123"
print(int(num)) 
print(type(num))
num = int(num) #converting string to integer
print(type(num))

#string functions
#1. len() function

greeting = "Hello"

print(len(greeting)) #5

greetings_2 = "Hello World"
print(len(greetings_2)) #11, a whitespace is also counted as a character

len_greet = len(greetings_2)

#in, not in

print("H" in greeting) #True
print('@' in greeting) #False
print('h' not in greeting)

#string concatenation using operators

first_name = "John"
last_name = "Doe"

full_name = first_name +" " + last_name

print(full_name)#John Doe

#use the * operator to repeat a string

name = first_name * 3
print(name)#JohnJohnJohn

#String Indexing
#Strings can be indexed (subscripted), with the first character having index 0.
#strings are immutable
#we use square brackets [] to index a string

hi = "Hello"

#Positive Indexing #starts from 0 from left to right
#H E L L O
#0 1 2 3 4

name = "John Njatha"

print(name[0]) #J
print(name[1]) #o
print(name[2]) #h
print(name[3]) #n

#Negative Indexing #starts from -1 right to left

name = 'John Njatha'
#J O H N  N J A T H A
#


print(name[-1])
print(name[-7])
print(name[-8])
print(name[-11])

#string slicing
#we use the colon operator to slice a string- [start:stop-1]

name = "John Njatha"
print(name[0:4]) #John 0,1,2,3
print(name[0:2]) #Jo
print(name[6:11])#Jatha 6,7,8,9,10
print(name[0:])#printing from index 0 to the end

#negative slicing
print(name[-6:-1])
print(name[-11:])
print(name[:-1])


#STRING METHODS
#1. upper() method
#converts a string to uppercase

name= ' john '
print(name.upper()) #JOHN
print(name.lower()) #john
print(name.isnumeric())#False
print(name.isalpha())#True
print(name.capitalize())#John
print(name.strip())#removes whitespaces from the beginning and end of a string


name = "John Njatha"

name = name.replace('Njatha', 'Wango')

print(name)


#String formatting

first_name = "Joy"
second_name = "Njanja"
age= 60

#using the + method    

print('my name is'+ first_name + ' ' + second_name + ' and I am ' + str(age) + ' years old')

#using the join method

print("my name is" + " ".join([first_name, second_name]) + "and I am" + str(age) + "years old") 
    
#using the format method

print("my name is {} {} and I am {} years old".format(first_name, second_name, age)) 
    
#using f-strings

print(f"my name is {first_name} {second_name} and \n I am {age} years old")   
    
  
    
    
    
    
    
    
    