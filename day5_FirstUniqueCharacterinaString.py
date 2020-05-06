'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


soluion:
class Solution:
    def firstUniqChar(self, s: str) -> int:
        alph = {}
        for cc in s:
            alph[cc] = alph.get(cc,0) + 1

        for i in range(len(s)):
            if alph.get(s[i]) == 1:
                return i
        return -1

'''
