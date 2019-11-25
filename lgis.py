# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:13:00 2019

@author: Rosa
"""
from __future__ import print_function
import os
import operator


def lgs(s, op=operator.lt):
    L = [0] * len(s)
    P = [None] * len(s)

    max_length = 0
    for i in range(len(s)):
        it = ((L[j] + 1 if op(s[j], s[i]) else 1) for j in range(i + 1))
        P[i], L[i] = max(enumerate(it, 0), key=operator.itemgetter(1))
        if L[i] == 1:
            P[i] = -1
        if L[i] >= max_length:
            pos, max_length = i, L[i]

    ls = []
    while pos > -1:
        ls.append(s[pos])
        pos = P[pos]

    return ls[::-1]


def lgis(s):
    return lgs(s, op=operator.lt)


def lgds(s):
    return lgs(s, op=operator.gt)


if __name__ == "__main__":
    with open ('rosalind_lgis (2).txt') as dataset:
        n = int(dataset.readline().strip())
        p = [int(r) for r in dataset.readline().strip().split()]

    print(*lgis(p))
    print(*lgds(p))