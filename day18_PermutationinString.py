'''
Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

solution:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1= ''.join(sorted(s1))
        dis1={}
        dis2={}
        for i in s1:
            if i in dis1.keys():
                dis1[i]+=1
            else:
                dis1[i]=1
        for j in range(0,len(s2)-len(s1)+1):
            k=s2[j:j+len(s1)]
            k= ''.join(sorted(k))
            for i in k:
                if i in dis2.keys():
                    dis2[i] += 1
                else:
                    dis2[i] = 1
            if dis1==dis2:
                return True
                break
            else:
                dis2={}
        return False


'''
