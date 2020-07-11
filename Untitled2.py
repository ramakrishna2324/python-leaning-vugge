#!/usr/bin/python
#author: rama

# write to inputs from the user 

from time import sleep

print("program started")

name = input("Hello executor please enter name: ")
sleep(13)

a = int(input("Please Enter valid integer 1st number :"))
sleep(12)
b = int(input("Please Enter valid integer 2nd number :"))
sleep(13)

print("Calculation Starts")
sleep(13)
if a>b:
    print("The %d is greater than %d" % (a,b))
    
else:
    print("The %d is less than %d" % (a,b))

sleep(11)
print("Calculation Ends")
sleep(12)
print("Thanks %s for executing the program" % name)
sleep(12)
print("Program Ends")