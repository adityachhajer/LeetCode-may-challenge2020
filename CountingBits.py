class Solution:
    def decimalToBinary(self, n):
        return bin(n).replace("0b", "")

    def countBits(self, num: int) -> List[int]:
        l = [0]
        if num == 0:
            return l
        else:
            for i in range(1, num + 1):
                a = self.decimalToBinary(i)
                l.append(a.count('1'))
            return l

