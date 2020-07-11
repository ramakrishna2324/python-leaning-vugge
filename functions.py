#!/usr/bin/python

# Autor: Rama
# Date : 26 Jun


print("Running out of functions")


# just print statement function defined
def prin_me():
    print("This iss first test line printing")
    print(" This sis second test line printing")
    print(" This is third test line printing")
    pass


# just add two number as arguments.
def add_me(first_num, second_num):
    print("First Number is  %d " % first_num)
    print("SEocnd Number is %d" % second_num)
    add_value = first_num + second_num
    return  first_num, second_num, add_value
   


#This is main function defni
def main():
    add_me(5, 10)
    prin_me()
    
    # second time
    prin_me()
    a = 10 
    b = 20
    add_me(a,b)
    
    
    # method with return and third time
    a = 100
    b = 200
    first_num, second_num, output_value = add_me(a, b)
    print(output_value)
    print("Added Values of %d and %d is %d" % (first_num, second_num, output_value))

 

# This is imain program
main()





