#Arithmetic operators
#+,-,*,/
x= 10
y=5
print(x+y)
print(x-y)
print(x*y)
print(x/y)
#exponential **,modulo %, integer division //
print(2**4) # exponential/power
# modulo, returns the remainder
print(5%2) 
print(4%2)
print(11%3) #returns 2 since its 3 remainder 2

print(10//5)
print(5//10)
print(17//10)

#Assignment Operators
#=,+=,-=
x=5#we are assigning the value 5 to x
name= "Linda" #we are assigning the value linda to name
print(name) # returns linda

#+=
#x=x+10 #is the same as
x+=10
x-=2
print(x)

#Relational operators
# these are used to compare values of operands.
#they return a booleon (either True or False)
# >,<,>=,<=,==,!=
x=10
y=5
z=10
print(x>y)
print(x<=y)
print(z==x)

#Logical operators
# these are operators used to combine conditional statements
print(x>y and z==x)
print(x>y and z==x or x<=y)