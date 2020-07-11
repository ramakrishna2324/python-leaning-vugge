#!/usr/bin/python

import conversion
'''

Excepiton Handling

To handle the error is good mananer , program should be defined with try ...except exception handler


Syntax:
    
    try:
        Block of tatements
        Statement2
        Statement3
        ...Statement3
    except Exception as e:
        print(e)
    '''

try:
    f = open("file1.txt", "r")
    first_num = input("Enter Value: ")
    second_num = 150
    
    test = conversion.gall_liter(first_num)
    print(test)
    
    
    
    # if first_num == "ram":
    #     raise Exception("this is ram error")
    
    # sum_value = int(first_num) + second_num
    
    # print(sum_value)
    
    # print("file Opened")
    # #f.write("hello World")
    

except TypeError:
    print("Hello, YOu have to enter only numeric")
    
except IOError:
    print("unable to open a file no such file")

except Exception as c:
    print(10+20)
    print("Something Wrong, Better Run again...")
    print(c)
    
else:
    print("No idea what to type here")

finally:
    f.close()
    print("This is final tatement will execute at any cost")
