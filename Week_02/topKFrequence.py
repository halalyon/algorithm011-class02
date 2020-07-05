class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict ={}
        nums.sort()
        length = len(nums)
        for i in nums:
            dict[i] = dict.get(i,0)+1
        dict = sorted(dict.items(), key=lambda dict:dict[1], reverse=True)
        res = []
        for x, y in dict:
            res.append(x)
        return res[:k]