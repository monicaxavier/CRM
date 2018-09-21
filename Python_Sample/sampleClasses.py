#Classes Pyhton

#Python is an object oriented programming everything in python is an object.

#Create  a class

#To create a class, use the keyword 'class'

class Name:
    x= 'Moni'
print(Name)

#to print the name we can craete an object like this

class Name:
 x = 'Moni'

obj = Name   #-->creating object obj
print(obj.x)  #-->printing the name by object

#output - Moni

#__init__() function
#All classes have a _init_() function, which is always executed when the class is being initiated.

class Moni:
	def __init__(self,age,interest):  #-->defining init()
	    self.age = age
	    self.interest = interest

obj = Moni(23, 'Piano')       #-->creating object
print(obj.age)                #-->calling by object
print(obj.interest)	      #-->calling by object

#output--> 
23
Piano

"""
to understand the __init__() method in better way, assume we are going to an ATM. when we insert the the card it displays our name and 
details. so what __inti__() is doing here, when the card is inserted the first class will get loaded. if we declare the __init__() 
method in the first class to get the details of the person who inserted the card, the__init__() method will go and get the details from 
the database or some other classes.so the __init__() is always executed when the class is being initiated.

"""

