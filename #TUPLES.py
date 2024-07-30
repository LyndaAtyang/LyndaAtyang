#TUPLES
#A tuple is a collection data type that is ordered and unchangeable
#  In Python tuples are written with round brackets.()

#a tuple is immutable, meaning you cannot change,
# add or remove items after the tuple has been created
lst = [1,1,1,2,2,2,3,4,5]

lst[0] = 0
print(lst)

num = (1,1,1,2,2,2,3,4,5)
# num[0] = 0  
# print(num) #TypeError: 'tuple' object does not support item assignment

print(num.count(1)) #2 #count() method returns the number of times a specified value appears in the tuple

# for i in num:
#     print(num.count(i))

print(num.index(1)) #0 #index() method returns the position at the first occurrence of the specified value


#SETS
#A set is a collection data type that is unordered, unindexed and of unique items.
#Unlike lists and tuples sets do not allow duplicate items and do not maintain the order of elements.
#In Python sets are written with curly brackets {} or the set constructor set().

names = {'John', 'Jane', 'Jack', 'Jill','Jack'}
print(names) #{'Jane', 'John', 'Jill', 'Jack'} #duplicate items are removed
print(type(names)) #<class 'set'>

#Set methods
names.add('Joe')
print(names) #{'Joe', 'Jane', 'John', 'Jill', 'Jack'}

names.update(['Jim', 'Joy'])
print(names) #{'Jim', 'Joe', 'Jane', 'John', 'Jill', 'Jack', 'Joy'}

names.remove('Joe')
print(names) #{'Jim', 'Jane', 'John', 'Jill', 'Jack', 'Joy'}

names.pop() #removes the last item
print(names) #{'Jane', 'John', 'Jill', 'Jack', 'Joy'}

names.clear()
print(names) #set()

st1 = {1,2,3,4,5}
st2 = {4,5,6,7,8,True}

#1. UNION- returns a set containing all the items from both sets
st3 = st1.union(st2)
st3 = st1 | st2
print(st3) 

#2. Intersection- returns a set containing the items that are present in both sets
st4= st1.intersection(st2)
st4 = st1 & st2
print(st4) #{1, 4, 5}

#3. Difference- returns a set containing the items that are present in the first set but not 
# in the second set
st5 = st1.difference(st2)
st5 = st1 - st2
st6 = st2-st1
print(st5) #{ 2, 3}
print(st6) #{8, 6, 7}

#4. Symmetric Difference- returns a set containing all the items that are not present in both sets

st7 = st1.symmetric_difference(st2)
st7 = st1 ^ st2
print(st7) #{ 2, 3, 6, 7, 8}

#DICTIONARIES
#We create dictionaries using curly brackets {} or the dict() constructor
#Dictionaries are collections of key-value pairs
#Keys areunique and immutable, and can be strings or literals, values can be of any data type
#we separate keys and values with a colon :

student = {'name':'John', 'age':24 }

codes = {"John":123456, "Jane": 789456, "Jack": 456123}

city= dict(name='Nairobi', population= 4_000_000)

city2 = { 1:"Nairobi", 2:"Mombasa", 3:"Kisumu" }


teacher = {'name': "Joy Owiyo",
           'age': 30,
           'residence':['Nairobi', 'Kisumu'],
           'subjects': {'Maths': 'Form 1', 'English': 'Form 2'},
           'students': ('John', 'Jane', 'Jack'),
            'is_teaching': True,
           'salary': None
}


#Accessing items
#You can access the items of a dictionary by referring to its key name
print(teacher['name']) #Joy Owiyo
#we can also use the function get()
print(teacher.get('age')) #30

#Changing values- keys are immutable, but values can be changed
#We use the keys to change the values of a dictionary
teacher['age'] = 35
print(teacher)

teacher['subjects']['Maths'] = 'Form 3'
print(teacher)

teacher['residence'].append('Nakuru')
print(teacher)


#Dictionary methods
codes = {"John":123456, "Jane": 789456, "Jack": 456123}
print(codes.keys())
print(codes.values())
print(codes.items())

codes.update({"Jim": 789456})
print(codes)

codes.pop('John')
codes.popitem() #removes the last item
print(codes)

keys = [1.0,1.1,1.2,1.3]
values = ['one', 'two', 'three', 'four']
dictionary = dict(zip(keys, values))
print(dictionary)