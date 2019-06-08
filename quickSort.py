# -*- coding: utf-8 -*-

import random
def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot_element = random.choice(arr)
    small = [i for i in arr if i < pivot_element]
    medium = [i for i in arr if i == pivot_element]
    big = [i for i in arr if i > pivot_element]
    
    return qsort(small) + medium + qsort(big)