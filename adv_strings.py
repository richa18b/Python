import random
import sys
import os

long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4])

print(long_string[-5:]) #Print starting from last five characters till the end

#Print from the beginning and end before the last five characters
print(long_string[:-5])

print(long_string[:4],"be there")

print("%c is my %s character"%('R','favourite'))

print("%d s my %s number"%(1,'favourite'))

print("%.5f is my %s decimal"%(.14,'favourite'))

#To capitalize the first letter of a string
print(long_string.capitalize())

#To find the index of a word in a string
print(long_string.find("Floor"))

print(long_string.isalpha())

print(long_string.isalnum())

print(len(long_string))

print(long_string.replace("Floor","Ground"))

'''
.strip() removes all whitespace at the start and end,
including spaces, tabs, newlines and carriage returns
'''

print(long_string.strip())

#Splitting a string into a list
#We specify how the string is supposed to be splitted like " " here
quote_list = long_string.split(" ")
print(quote_list)