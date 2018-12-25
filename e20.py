# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 08:01:00 2018

@author: Rahul
"""
from math import factorial

n = factorial(100)

li = [int(d) for d in str(n)]

print(sum(li))