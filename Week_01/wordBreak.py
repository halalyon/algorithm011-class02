from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = {elem: idx for idx, elem in enumerate(wordDict)}
        size = len(s)
        dp = [False] * (size+1)
        dp[0] = True
        for i in range(1, size+1):
            for j in range(i):
                if dp[j] and s[j:i] in wd:
                    dp[i] = True
                    break
        return dp[size]