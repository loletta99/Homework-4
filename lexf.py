# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:26:54 2019

@author: Rosa
"""
from itertools import product
f = open("rosalind_lexf (5).txt", 'r')
a = list(f.readline().rstrip().split())
n = int(f.readline().rstrip())
f.close()

for perm in product(a, repeat=n): 
    print( "".join(perm))

