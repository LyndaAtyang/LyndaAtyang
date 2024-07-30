
import math


x= 16
y= math.sqrt(16)
print(y)

x= 2
print(math.fabs(x)) #returns the positive

print(math.pow(2,3)) # returns two power 3,
#requires two arguments

print(math.sin(30))
print(math.cos(30))
print(math.tan(10))
print(math.log(1))

y= 2.8
z= 2.2

print(math.ceil(z))# returns the smallest integer greater than or equal to z
print(math.floor(y))# returns the largest integer less than or equal to y

#import as alias

import math as m

x= 16
print(m.sqrt(x))
print(m.ceil(y))

from math import *

print(sqrt(x))
print(ceil(y))
print(floor(z))

from math import pi,e

print(pi)
print(e)

