#!/usr/bin/python

# Autor: Rama
# Date : 27 Jun

def hr_mi(hours):
    min = hours * 60
    print(min, "minutes")
    return hr_mi
    
def km_mil(kmh):
    mph =  float(0.6214 * kmh)
    print("Speed:  %d KM/H =  %f MPH" % (kmh, mph))
    return km_mil
    
def pou_kilo(kilo_grams):
    pounds = kilo_grams * 2.2046
    print('%d Kilograms = %f  Pounds' % (kilo_grams, pounds))
    return pou_kilo
    
def gall_liter(liters):
    try:
        gallon = liters /3.785411784
        print("%f liters is equals to %f gallons" % (liters, gallon))
        return gall_liter
    except TypeError:
        return "Invalid input has given"
    
def cm_inch(cm):
    inc = cm/2.54 
    print("Distance in %f : " % inc)
    return cm_inch
    
def Hws(kilo_watt):
    Hws = kilo_watt*0.75 
    print("hoursepower in kilowatts is %f " % Hws)
    return kilo_watt
    
def deg_rad(degres):
    pi = 22/7
    radius = degres*(pi/180)
    print(radius)
    return radius
    
def main():
    print("Starting the program")
    
    op =input('''To convert hours to minutes type 'time'
    To convert kilometres per hour to miles per hour type 'speed'
    To convert kilograms to pounds type 'mass'
    To convert litres to gallons type 'vol'
    To convert horsepower to kilowatts type 'power'
    To convert degree to radians type 'arc'
    Enter your choice : ''')
    
    if op == 'time':
        hours = int(input("Please enter hours: "))
        hr_mi(hours)
    elif op == 'speed':
        kmh = int(input("Enter km/h: "))
        km_mil(kmh)
    elif op == 'mass':
        kilo_grams = float(input('Enter weight in Kg to Convert into pounds: '))
        pou_kilo(kilo_grams)
    elif op == 'speed':
        liters = int(input("please enter no. of liters to convert into gallon: "))
        gall_liter(liters)
    elif op == 'vol':
        cm = float(input("Enter the distance measured in centimeter : "))
        cm_inch(cm)
    elif op == 'power':
        kilo_watt = float(input("Enter the hoursepower measured in kilowatts : "))
        Hws(kilo_watt)
    elif op == 'arc':
        degres = float(input("Input degrees: "))
        deg_rad(degres)
    
# Main Program   
# Boiler Plate Syntax  (_ = Underscore,  __ = Dunder)
if __name__ == '__main__':
    main()