
def twoSum(nums, target):
    hashed = {}
    for idx, ele in enumerate(nums):
        if ele in hashed:
            return [hashed[ele], idx]
        hashed[target - ele] = idx
        
        
        
        
print(twoSum([2,1,3, 7], 9))