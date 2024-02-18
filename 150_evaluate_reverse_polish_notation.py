class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for token in reversed(tokens):
            if token in ["+", "-", "*", "/"]:
                num1 = numbers.pop(0)
                num2 = numbers.pop(0)
                if token == "+":
                    numbers.insert(0, num1 + num2)
                elif token == "-":
                    numbers.insert(0, num1 - num2)
                elif token == "*":
                    numbers.insert(0, num1 * num2)
                else:
                    numbers.insert(0, int(num1 / num2))
            else:
                numbers.insert(0, int(token))
        return numbers.pop()
