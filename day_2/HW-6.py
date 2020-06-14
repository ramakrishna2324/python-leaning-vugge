#!/usr/bin/python
#author:rama
'''
take a String 
Show below outputs
1. Swapcase
2.andCaptilize
3. Title
4. Reverse
5. lower, lstrip, rstrip, uuper,casefold, center, count
'''
S = input("Please provide a string")

print(S.swapcase())
print(S.capitalize())
print(S.title())
reverse = S[::-1]
print(reverse)
print(S.lower())
lstrip = S.lstrip()
rstrip = S.rstrip()
print("this is used for", lstrip, "function")
print("this is used for", rstrip, "function")
print(S.upper())
#print(S.count(5))
print(S.casefold())
print(S.center())