a= 5
b=10

# a=b #b is 10
# b=a #b is 10
# print(a,b)

#introduce a temporary variable

temp= a
a=b
b= temp

print(a)
print(b)

#addition and sub
x=5
y=6

x=x+y
y=x-y
x=x-y

print(x,y)

#Uses ROT TWO ROTATION concept
#Most efficient way to swap variables

a=5
b=20

a,b=b,a
print(a,b)
