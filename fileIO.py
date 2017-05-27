import random
import sys
import os

test_file = open("test.txt","wb") #To create as well as open a file

print(test_file.mode)
print(test_file.name)

#Writing into a file
test_file.write(bytes("Write me to the file\n",'UTF-8'))

test_file.close()

test_file = open("test.txt",'r+') #Opening a file in reading and writing mode

print(test_file.read())

os.remove("test.txt")