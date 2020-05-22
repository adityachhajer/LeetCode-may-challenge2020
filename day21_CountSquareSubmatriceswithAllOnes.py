'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.


solution:

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        a=[[0]*(m+1)for _ in range(n+1)]
        count=0

        for row in range(1,n+1):
            for col in range(1,m+1):
                if matrix[row-1][col-1]==1:
                    a[row][col]=1+min(a[row][col-1],a[row-1][col],a[row-1][col-1])
                    count+=a[row][col]

        return count
'''