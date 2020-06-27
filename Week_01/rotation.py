class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        steps = k % size
        if steps == 0:
            return
        else:
            nums[:-steps], nums[-steps:] = nums[-steps:], nums[:-steps]
            return