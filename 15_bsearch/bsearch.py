"""
Binary search in a sorted array

Author: JesseJMa
"""

from typing import List

def bsearch(nums: List[int], target: int) -> int:
    """
    Binary search of a target in a sorted array
    without duplicates. If such a target does not exist,
    return -1, othewise, return its index.
    """
    
    left = 0
    right = len(nums) - 1
    mid = left + (right - left) // 2
    
    while left <= right: 
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
            
    