#!/usr/bin/env python
# -*- coding: latin-1 -*-
"""
Attribute -> Object -- charactertistic
        Christian Attributes -> Virtues -> Patience, Self-control, love,
        St.Augustine's attributes -> Patience, Self-control (33), love
        Object -> Attributes -> Clock -> methods, attributes
        [Abstract][Man][Age][Name][concrete]->Rick[Name][Age]
        [Abstract-object][Abstract-art]
        [Very-Good] -> Music Notation -> Play
        [Notation][Abstact represention of music ][10 nation]-> combination -> millions
        ->[Bekman][Concrete][Song1][Song2][Song3]
        -> [Sub-routine][Function][Function]


Function (X)->Y
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Rick", 90)
p2 = Person("Muthu_Thevar", 33)
p3 = Person("Kamarajar_Nadar", 55)
p4 = Person("John_pandian", 90)

print (p4.name)
