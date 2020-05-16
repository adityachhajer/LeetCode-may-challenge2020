class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        l = []
        maxsum = totalsum = A[0]
        for i in A[1:]:
            maxsum = max(i, maxsum + i)
            totalsum = max(totalsum, maxsum)
        k = totalsum
        c = sum(A)
        for i in A:
            l.append(-1 * i)
        maxsum = totalsum = l[0]
        for i in l[1:]:
            maxsum = max(i, maxsum + i)
            totalsum = max(totalsum, maxsum)
        c = c + totalsum
        if c > k and c != 0:
            return c
        else:
            return k




