
# Given an integer array nums, 
# return all the triplets 
# [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
# and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. 
# You may return the output and the triplets in any order.


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1 
            right = len(nums)-1
            while left <right:
                total = nums[i]+nums[left]+nums[right]
                if total ==0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left <right and nums[left] == nums[left +1]:
                        left +=1 
                    while left <right and nums[right] == nums[right -1]:
                        right -= 1
                    left +=1 
                    right -=1
                elif total<0 :
                    left +=1
                else:
                    right -= 1
