class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        sub = deque([])
        left = 0
        result = 0
        for r in range(len(s)):
            if s[r] in sub:
                pop = None
                while s[r] != pop:
                    pop=sub.popleft()
                    left +=1
            sub.append(s[r])
            result = max(result, r-left+1)
        return result
