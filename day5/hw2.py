#!/usr/bin/python
#author=ram

'''
Write aprogram, get a value from the user,
and ask him to convernt farehn, cel and convert it based on it.

'''
print("program started")

temp = int(input("Enter temperature : "))

option = input("enter cel (0)/ far(1): ")

if option == 0:
    print("converting given input to celsius")
    
    cel = (temp - 32) * 5.0/9.0
    print(cel)
else:
    print("converting given input to farhrenheit")
    far = (int(temp)*1.8) + 32
    print(far)