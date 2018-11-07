#Module is nothing but a python library
#we can save the module as .py and import in our code.
"""Example
Save this code in a file named mymodule.py """

def greeting(name):
  print("Hello, " + name)

  """Use a Module
Now we can use the module we just created, by using the import statement:

Example
Import the module named mymodule, and call the greeting function:"""

import mymodule

mymodule.greeting("Jonathan")

#when using the function from the module use the syntax module_name.function_name

#using dictionary

moni = {  "instrument" : "piano", "sport" : "Tennis" }

"""saves this code as monimodule.py and access the dictionary as below"""

import monimodule
a = monimodule.moni["instrument"]
print(a)


#Renaming a module
#we can rename a module as we want, use as keyword to change the module name

import monimodule as mmdl
a = mmdl.moni["instrument"]
print(a)


"""There are several built-in modules in Python, which you can import whenever you like.


Import and use the platform module:"""

import platform

x = platform.system()
print(x)

"""Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

List all the defined names belonging to the platform module:"""

import platform

x = dir(platform)
print(x)

#Import from module
#we can import a part of a module by using a *****from***** keyword
#The module named mymodule has one function and one dictionary:
  
def greeting(name):
  print("Hello, " +name)
  
moni = {  "instrument" : "piano", "sport" : "Tennis" }

#Import only the moni dictionary from the module:

from mymodule import moni
print(moni["instrument"])

