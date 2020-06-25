#!/usr/bin/python
#author: rama
'''
Write a Program , 
get 2 values, and an operator 
from the user ( +, -, * , / ) 
and check iwhat operator it is and runn 
the oeprations accordingly.
'''
print("program started")

values_1 = int(input("enter a 1st number for arthematic operation:  "))
values_2 = int(input("enter a 2nd number for arthematic operation:  "))

operator = input("enter any  operator to execute values_1 and values_2: ")

print("Calculation Starts")

if operator == '+':
    execute = values_1 + values_2
    print(execute)
    
if operator == '-':
    execute = values_1 - values_2
    print(execute)
    
if operator == '*':
    execute = values_1 * values_2
    print(execute)
    
if operator == '/':
    execute = values_1 / values_2
    print(execute)
