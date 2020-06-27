from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        First solution O(n^2)
        """
        # j = 0
        # size = len(nums)
        # for i in range(0, size):
        #     if nums[i] == 0:
        #         for j in range(i+1, size):
        #             if nums[j] != 0:
        #                 nums[i], nums[j] = nums[j], nums[i]
        #                 break
        #         if j == size-1:
        #             break
        """
        Second solution O(n)
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

if __name__ == "__main__":
    ins = Solution()
    nums = [0,1,0,3,0,12]
    ins.moveZeroes(nums)
    print(nums)