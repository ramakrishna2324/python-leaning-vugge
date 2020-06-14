#!/usr/bin/python

'''
1. Take a input from user
2. Show them celsius to fahren converting
3. Taka input from user4. 
4. show them fahren to celsius
'''

# Taking input as celsius from user
c = input("Enter temperature(in celsius) : ")

# converting to fahrenheit
f = (int(c)*1.8) + 32
print("The temperature in fahrenheit is %0.3f" % f)

# Taking input as Fahrenheit from user
f = int(input("Enter temperature(in Fahrenheit) : "))

# converting to celsius
c = (f - 32) * 5.0/9.0

print("The temperature in celsius is %0.3f" % c)
