class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def helper(s):
            if not s:
                return True
            for word in wordDict:
                if s[:len(word)] == word and helper(s[len(word):]):
                    return True
            return False

        return helper(s)
