#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
   def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = x < 0 and -1 or 1
        print(sign)
        x = abs(x)
        ans = 0
        while x:
            print(ans)
            ans = ans * 10 + x % 10
            x = x // 10
        return sign * ans if ans <= 0x7fffffff else 0
                
            
        
        


    
        
        

