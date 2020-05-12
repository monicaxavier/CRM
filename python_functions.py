while loop

i=1
while(i<6):
    i +=1
    if(i==3):
        continue
    print(i)
output--> 2,4,5,6

Functions in python
defining a function using "def" keyword
def myfirst_prog():
print('My First Program')

calling the function
def myfirst_prog():
    print('My First Program')
     
myfirst_prog()
output--> My First Program

Parameters
**Data or information can be passed to functions as parameters
**parameters are specified after defining functions inside the parameters, we can include as many parameters as we want, we need to separate in by comma.

Prog:
def myfirst_prog(fname):
    print(fname +' Xavier')
    
myfirst_prog('John')
myfirst_prog('Emalda')
myfirst_prog('Monica')
**output**
John Xavier
Emalda Xavier
Monica Xavier

Default Parameter Value
If you dont specify the passing values it will automatically use the default parameter
prog:

def countries_name(country = 'America'):
    print('Hello ' +country)
countries_name('England')
countries_name('Canada')
countries_name('France')
countries_name( )
**output**
Hello England
Hello Canada
Hello France
Hello America

Return function
to let a function  return a value we can use return() function

def calculation(val):
    return  5 * val
print(calculation(3))
print(calculation(4))
print(calculation(5))
**output**
15,20,25
we can write this program without return like this
def calculation(val):
    print( 5 * val)
calculation(3)
calculation(4)
calculation(5)
**output**
15,20,25

Lambda Function in Python
A lambda function can take multiple arguments but only one expression
1)prog:
x = lambda a : a + 10 --> (a will be 10)
print(x(10))
**output** 
20
2)prog:
x = lambda a,b : a * b
print(x(10,7))
**output**
70
3)prog:
x = lambda a,b,c : a * b + c
print(x(10,7,2))
**output**
72

why to use lambda?
it is useful when we use lambda as an anonymous function inside  another function
let say we have a function that takes one argument and it will be multiplied with an unknown number
prog:
def moni_func(x):
    return lambda y : y + x
    
another_value = moni_func(5)
print(another_value(4))
**output**
9
