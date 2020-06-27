class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        while digits:
            elem = digits.pop()
            result = elem + carry
            if result == 10:
                carry = 1
                res.insert(0, 0)
            else:
                res.insert(0, result)
                carry = 0
                continue
        if res[0] == 0: res.insert(0,1)
        return res 