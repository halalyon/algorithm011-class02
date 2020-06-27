from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        size = len(nums)
        i = 0
        while i < size-2:
            target = -nums[i]
            l = i + 1
            r = size - 1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else: 
                    lower = nums[l]
                    upper = nums[r]
                    res.append([nums[i], lower, upper])
                    # delete repeated l
                    while l < r and nums[l] == lower:
                        l += 1
                    # delete repeated r
                    while l < r and nums[r] == upper:
                        r -= 1
            i += 1
            # delete repeated i
            while i < size-1 and nums[i] == nums[i-1]:
                i += 1
        return res