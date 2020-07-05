class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in res:
                return [res[comp], i]
            res[nums[i]] = i