"""
Bubble sort, Insertion sort and Selection sort

Author: JesseJMa
"""

from typing import List

def bubble_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    
    
    for i in range(length):
        made_swap = False
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                made_swap = True
            if not made_swap:
                break

def insertion_sort(a: List[int]):
    length = len(a)
    if length <= 1:
        return
    
    for i in range(1, length):
        value = a[i]
        
        j = i - 1
        
        while j > 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
            
        a[j] = value
            
    