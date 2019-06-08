#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}   
        for idx, ele in enumerate(nums):
            if ele in hashed:
                return [hashed[ele], idx]
            hashed[target - ele] = idx
                
        
        

