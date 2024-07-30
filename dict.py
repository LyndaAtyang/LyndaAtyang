#Dictionaries
#A dictionari in python is a collection data type that is mutable and indexed.
#Dictionaries store data in key-value pairs.
# Keys are unique and associated with a value.
# Keys are typically immutable data types, like 
#strings and literals, while vaues can be of any data type.

#strings are defined by enclosing key value pairs within 
# curly braces #or using the dict constructor

student = {'name':'Joy','age':20, 'city':'Nairobi'}

phones = {'Linda':'Samsung', 'Vic':'Iphone', 'Fay': 'OnePlus'}

city = {1:'Nairobi', 2:'Mombasa', 3:'Kisumu', 4:['Eldy','Naks']}

#Accessing Items in a dictionary
#we access items using keys

print(city[1])
print(phones['Vic'])
print(student['age'])

#using get()fuction
print(phones.get('Fay'))
print(city.get(3))

#Changing values in a dictionary
#we use the keys to change the value in a dictionary

student['age'] = 18
print(student)

phones['Vic'] = 'Infinix'
print(phones)

#Dictionary methods
print(phones.keys())
print(city.values())
print(phones.items())

student = {'name':'Joy','age':20, 'city':'Nairobi'}

student.update({'lesson':'Python'})
print(student)

student.pop('age')
print (student)

student.popitem()
print(student)

keys = [1.0,1.1,1.2]
values = ['Python','C++','Java']

lessons = dict(zip(keys,values))
print(lessons)