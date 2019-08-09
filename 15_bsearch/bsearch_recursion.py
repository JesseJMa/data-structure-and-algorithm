"""
Binary search in a sorted array
An implement based on recursion

Author: JesseJMa

"""

from typing import List

def bsearch(nums: List[int], target: int) -> int:
    return bsearch_internally(nums, 0, len(nums) - 1, target)


def bsearch_internally(nums: List[int], low: int, high: int, target: int) -> int:
    if low > high:
        return -1
    
    mid = low + (high - low) // 2  # can be selected as you like, but must be in the scope between low and high
    
    print('mid ==', mid)
    
    if nums[mid] == target:
        return mid
    
    elif target < nums[mid]:
        return bsearch_internally(nums, low, mid - 1, target)
    else:
        return bsearch_internally(nums, mid + 1, high, target)
    
    
    
    
    
result = bsearch([1,3,4,7,10], 4)
print('result = ', result)