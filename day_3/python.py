
'''
Datatypes

1. list
2. tuple
3. Dictionary 

List - Array
will be denoded as []
Data inside [] are separated by comm (,)
Any datatype data's as an element
Elements can be changeable
Example :
var1 = []
var2 = [5,6,7,8,9,0]
var3 = ['a', 'b', 'c']
var4 = ['ram', 'dhana', 'india']
var5 = ['ram', 5, 'eng', 98]
var6 = ['ram', var2, 'eng', 99]   is equal to ['rama', [5,6,7,8,9,0], 'eng', 99]

Read the Eleements, by indexing

print(var6[0])  --> 'ram'

var6.append('langu')
newvar = list()



Tuple:

Tuple is immutable of list  ( Read Only))
Tuple is denoted with ()
Elements are not changeable
But, You can combine tuples

You retreive the elements by pos value
But nothing can be modified

Example:

tup_var1 = ()
tup_var2 = (4,5,6,7,89)
tup_var3 = ('a','b','c')
tup_var4 = ('Ram', "dhana', 'india')
tup_var5 = ('Ram', 5, 6, 'USA')
tup_var6 = ("Ram", tup_var4, 100)

'''