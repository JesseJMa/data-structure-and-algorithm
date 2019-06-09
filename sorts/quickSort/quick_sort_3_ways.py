# -*- coding: utf-8 -*-
from __future__ import print_function
import random
# import insertionSort
def quick_sort_3partition(sorting, left, right):
    if left > right:
        return
    a = i = left
    b = right
    pivot = random.choice(sorting)
    
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[i], sorting[b] = sorting[b], sorting[i]
            b -= 1
        else:
            i += 1
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)
            
myList = [49,38,65,97,76,13,27,49, 10, 0,0,0,0,0,0,0,0,0,0,0,0,0,0]
quick_sort_3partition(myList, 0, len(myList) - 1) 
print(myList)

