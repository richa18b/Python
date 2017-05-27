import random
import sys
import os

grocery_list = ['Tomatoes','Potatoes','Juice','Bananas','Carrot']

print(grocery_list)

#Accessing ith item in the list
print("First item is ",grocery_list[0])

#Changing ith item in the list
grocery_list[0] = 'Apples'
print(grocery_list)

print(grocery_list[1:3]) #Print items in the index range [1,3)

#lists inside a list
other_events = ['Wash car','Check cash','Meet Da']

to_do_list = [grocery_list,other_events]
print(to_do_list)

#Accessing a specific item in a list of lists
print(to_do_list[1][1])

#Other operations
grocery_list.append('Cucumber')
grocery_list.insert(2,'Mangoes')
grocery_list.remove('Bananas')

print(grocery_list)

#Sorting list
grocery_list.sort();
print(grocery_list)

grocery_list.reverse(); #Reverse Sort
print(grocery_list)

#Deleting
del grocery_list[3]
print(grocery_list)

#Adding lists
to_do_list2 = grocery_list + other_events
print(to_do_list2)

print("length of to_do_list2 = ",len(to_do_list2))
print(max(to_do_list2)) #Prints max alphabetically here
print(min(to_do_list2))