#!/usr/bin/python
#author:rama

'''
question:1. Take a 3 inputs from users  as hours, minutes, seconds
2. Show that the formatted output and tootal seconds.
'''

H = int(input("Please enter hr Hours: ")) 
M = int(input("Please enter hr Minutes: "))
S = int(input("Please enter hr seconds: "))

#Formatted output od time
print("The time which you entered is %dH:%dM:%dS" %(H,M,S))


Hours = H * 60 * 60

Minutes = M * 60

#Total time
time = Hours + Minutes + S

print("Total no of secs=",time)