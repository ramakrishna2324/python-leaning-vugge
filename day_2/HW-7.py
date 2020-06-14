#!/usr/bin/python
#author:rama
'''
str
rfind, rindex, isdigit, is lower, isnumeric, isprintable, isspace, isuuper
'''
S = "my name is rama krishna"

find = S.rfind("name")

print(S.isdigit())# It returns true or false if all characters int he string are digits
print(find)
print(S.rindex("rama"))
print(S.isdigit())
print(S.islower())
print(S.isnumeric())
print(S.isprintable())
print(S.isspace())
print(S.isupper())