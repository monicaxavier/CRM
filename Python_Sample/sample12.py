Tuple(Collection)
--> same like List but it cannot be changed
ex1:
Tuple = ('John','Xavier','Emalda')
print(Tuple)
--->('John','Xavier','Emalda')

Accessing tuples
print(Tuple[1])--> Xavier

We cannot change the values in the tuples as we did in list. even if you try to change the value is still the same.

looping
mytuple = ('apple','orange','grapes')
for k in mytuple:
	print(k)
->
apple
orange
grapes

Tuple length
mytuple = ('apple','orange','grapes')
print(len(mytuple))
-->3

Tuples are unchangeable, you cannot add/remove/update the tuple but you can delete the tuple completely.
using del keyword
mytuple = ('apple','orange','grapes')
del(mytuple)

we can create a tuple using tuple() method
mytuple = tuple(('mango','pomo'))
for x in mytuple:
  print(x)
-->
mango
pomo

Tuple methods
it has two built in methods
count()
index()

count()
mytuple = (1,2,6,8,4,2,7,9,2)
k=mytuple.count(2)
print(k)
ans -> 3

index()-->return the first occurance position of the given value
mytuple = (1,2,6,8,4,2,7,9,2)
k=mytuple.index(2)
print(k)
ans-->1

Set
same like other collection.
loop through the set
myset={'apple','banana','orange'}
print('banana' in myset)
ans-->true

Dictionary
mydict = {'name':'moni','age':23,'fname':'jesu'}
for x,y in mydict.items():
  print(x,y)
-->
name moni
age 23
fname jesu

mydict = {'name':'moni','age':23,'fname':'jesu'}
for x in mydict.values():
  print(x)
it will display values alone
moni
23
jesu

adding to dictionary
mydict = {'name':'moni','age':23,'fname':'jesu'}
mydict['company']='cts'
print(mydict)

to remove use del keyword

*****Loops in Python******
moni = 23
rick = 27
if moni > rick:
  print('moni is elder than rick')
else:
  print ('moni is younger than rick')

While Loop
**********
i = 1
while(i<6):
  print(i)
  i +=1
1 2 3 4 5
	

