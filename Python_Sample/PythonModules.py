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
