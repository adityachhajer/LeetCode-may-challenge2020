class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        t = []
        while (i < len(A) and j < len(B)):
            a = max(A[i][0], B[j][0])
            b = min(A[i][1], B[j][1])
            if a <= b:
                t.append([a, b])
            if A[i][1] >= B[j][1]:
                j += 1
            else:
                i += 1
        return t

