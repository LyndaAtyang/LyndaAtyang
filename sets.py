#TUPLES
#Atuple is a collection data type that is ordered and immutable.
#Tis means once a tuple is created, Its elements cannot be changed
#added or removed. 
#Tuples are defined by enclosing the elements with paranthesis
#(normal brcackets) and then separating by commas.

names = ('john','doe','jane','joy')

print(type(names))
print(names[0])

#Tuple methods
names.count('john')#returns the no of times the element appears
names.index('jane') #returns the index of the element

#SETS
#Sets is an unordered collection of unique elements. 
# Sets are defined within curly brackets and separated by commas. 
#Unlike lists and tuples, sets do not allow duplicate elements
#and do not maintain the order of elements
#Can also create with a set constructor

names = {'john','doe','jane','joy','joy'}
print(names)
print(type(names))

nums = set((20,18,26,43,10))
print(nums)

#SET METHODS
nums.add(11) # adds the element 11 in the set nums
print(nums)
nums.update([12,180,76])
print(nums)

nums.remove(180) #removes the element 180
nums.discard(20)

nums.pop()
print(nums)

nums.clear() #returns a blank set

#we can use inbuilt functions to perform certain operations on sets

st_1 = {1,2,3,4,5}
st_2 = {4,5,6,7,8}

#1. Union
#Union returns all the unique elements in both sets
print(st_1.union(st_2)) #{1,2,3,4,5,6,7,8} 4, and 5 only appear once
union_set = st_1|st_2

#2. Intersection
#Intersection returns al the common elements in both sets
print(st_1.intersection(st_2)) #{4,5}
union_set = st_1 & st_2

#difference
# Returns the different elements in the first set not in the second set
print(st_1.difference(st_2))#{1,2,3}
print(st_2.difference(st_1)) #{6,7,8}
union_set = st_1 - st_2


#symmetric difference
#We get the difference of the two sets, i.e elements that are not
#common in both sets
print(st_1.symmetric_difference(st_2)) #{1,2,3,6,7,8}
union_st = st_1 ^ st_2

