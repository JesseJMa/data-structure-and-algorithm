
def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if i < len(nums)-1 and nums[i] < target and nums[i + 1] > target:
            return i + 1
        pass
        
print(searchInsert([1,2,3,6], 5))