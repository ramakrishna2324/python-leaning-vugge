#!/usr/bin/python
#author:rama
'''
Write program
Take a Speed in KmPH
Conver the kmPh into miles per hours
'''

KM = float(input("enter speed in KMPH: "))

#conversion factor
conversion = 0.621371

miles = KM * conversion

print("one KM is equals to %f miles" %miles)
