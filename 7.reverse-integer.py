#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        arr = list(str(x))
        i = 0 if arr[0] != '-' else 1
        j = len(arr) - 1
        
        while i < j:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            i += 1
        
        result = arr if arr[0] != '0' else arr[1:]
        if result:
            return int(''.join(result))
        else:
            return None
        
        pass
        

