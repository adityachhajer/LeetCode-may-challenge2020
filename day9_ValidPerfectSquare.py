'''
Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false


solution:
hint-binary search

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==0:
            return False
        elif num==1:
            return True
        else:
            l=2
            u=(num//2)+1
            while(l<=u):
                mid=(l+u)//2
                if(mid*mid==num):
                    return True
                else:
                    if (mid*mid)>num:
                        u=mid-1
                    else:
                        l=mid+1
            return False

'''