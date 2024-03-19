class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {"{":"}","[":"]","(":")"}
        stack = []
        for char in s:
            if char in dictionary:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif dictionary[stack.pop()] != char:
                return False
        return not stack
