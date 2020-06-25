#!/usr/bin/python
#author:ram
'''
convert kilometers/h to miles/h
'''

kmh = int(input("Enter km/h: "))

mph =  float(0.6214 * kmh)

print("Speed:  %d KM/H =  %f MPH" % (kmh, mph))
