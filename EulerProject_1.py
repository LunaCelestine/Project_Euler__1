# -*- coding: utf-8 -*-
"""
Created on Sat May 18 16:48:29 2019

@author: AdrielleTheSlayer
"""


max = 1000

def count_by_three(max):
    i = 3
    results = []
    while i < max:
        results.append(i)
        i += 3
    return results

def count_by_five(max):
    k = 5
    results = []
    while k < max:
        results.append(k)
        k += 5
    return results
 

three = count_by_three(max)
five = count_by_five(max)     
quotients = set(count_by_three(max)) | set(count_by_five(max))
total = sum(quotients)
print(total)

