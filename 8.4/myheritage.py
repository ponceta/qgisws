#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3 ready
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

class Bag(object):
    """Une classe pour stocker des choses"""
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
        

class Charriot(Bag):
    """Une classe pour stocker les sacs"""
    def __init__(self):
        super(Charriot, self).__init__()
    def add2(self,x):
        self.addtwice(x)
        

b=Bag()
b.add("chaine")

c = Charriot()
c.add("genius")
c.add2("ali")


        
