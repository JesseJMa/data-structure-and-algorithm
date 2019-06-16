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

if __name__ == '__main__':
    
    arr = [3,5,6,1,8,7,7,2,0,1]
    print(qsort(arr))