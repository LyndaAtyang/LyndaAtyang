#SEQUENCES - LISTS
#Lists are an ordered collections of items, 
# which can be of different data types.

#Lists are created using square brackets or using the 
#list() constructor.

#Lists are mutable, meaning their elements can be changed

blank = [] #empty list
num = [1, 2, 3, 4, 5]
num2 = [1, 2, 3, 4, 5, "John", "Doe", True, False, 3.14]
names = ["John", "Doe", "Jane", "Doe"]
names2 = list(("John", "Doe", "Jane", "Doe"))
classes = ['Python', 'Java', 'C++', ['JavaScript', 'html', 'css']]   

print(type(num2))
print(type(names2))

#Accessing items in a list
#We use the index and [] to access an item in a list
#positive indexing starts from 0
print(num[3]) #4
print(num2[7])#True
print(names[2])#Jane

#Negative Indexing starts from -1
print(classes[-1])#['JavaScript', 'html', 'css']
#to access the nested list
print(classes[-1][-2])#html

#Slicing
#We can access a range of items in a list using slicing
#We use the colon : to slice a list

print(num2[2:5])#[3, 4, 5]

#string functions
print (len(num2)) #outputs the no.of items in the list

num = [1, 2, 3, 4, 5]
num1 = [6, 7, 8, 9, 10]

#concatenation
num3 = num + num1

print(num3) #returns [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2= num*3
print(list2) #returns [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

print(10 in num3)#True
print(11 in num3)#False

#List Methods

#name = "John"
# name_list = list(('John')) #['J', 'o', 'h', 'n']
# print(name_list)

name_list= ['John']
print(name_list) #['John']

name_list.append('Asaph')
name_list.append('Njatha')

print(name_list) #['John', 'Asaph', 'Njatha']

name_list.insert(1, 'Doe') #specify the index and the item to insert

name_list.remove('Asaph') #removes the specified item

name_list.pop() #removes the last item in the list

name_list.clear() #removes all items in the list []

list2 = num*3
print(list2) #returns [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

list2.reverse() #reverses the list

list2.sort() #sorts the list in ascending order

list2.sort(reverse=True)#sorts the list in descending order
print(list2)

list2.count(1) #counts the no. of times the specified item appears in the list
print(list2.index(1)) #returns the index of the specified item in the list #OUTPUT: 12

fl = [9.0,7,6,3.6,3.1]
fl1 = [1, 2, 3]

fl.extend(fl1) #adds the items in the specified list to the end of the current list
print(fl) #OUTPUT: [9.0, 7, 6, 3.6, 3.1, 1, 2, 3]

del fl[0] #deletes the item at the specified index

print(fl) #OUTPUT: [7, 6, 3.6, 3.1, 1, 2, 3]

del fl[0:3] #deletes the items in the specified range
print(fl) #OUTPUT: [3.1, 1, 2, 3]

#List Comprehension

#List comprehension is a concise way to create lists,
# or a shorter syntax to create a new list bases on the values 
# of an existing list.

basket = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

new_basket = [fruit for fruit in basket]

#for every fruit in fruits, if the fruit contains the letter 'a', add it to the new_fruits list
print(new_basket) #['apple', 'banana', 'cherry', 'kiwi', 'mango']

new_basket = [fruit for fruit in basket if 'a' not in fruit]
print(new_basket) #['cherry','kiwi',]

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_num = [n for n in num if n%2==0]
# n- elements in the new list from the num list if the element is 
# divisible by 2

basket = ['apple', 'banana', 'cherry', 'kiwi', 'mango','orange']

new_basket = [fruit for fruit in basket if fruit != 'mango']

new_basket = basket.remove('mango')

