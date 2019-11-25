# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:39:43 2019

@author: Rosa
"""
def fib(n,k):
    rabbits_vivi = [1, 1+k]
    for _ in range(n-2):
        offspring = k * rabbits_vivi[-2]
        rabbits_vivi.append(rabbits_vivi[-1] + offspring)
        
    return rabbits_vivi

print(fib(34,3)[-2])