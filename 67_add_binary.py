class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a,2), int(b,2)
        while True:
            result = x ^ y
            carry = (x & y) << 1
            x , y = result, carry
            if carry == 0:
                break
        return bin(result)[2:]
