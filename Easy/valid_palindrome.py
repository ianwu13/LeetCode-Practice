'''
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 2: dual pointer
        alpha_num = '1234567890qwertyuiopasdfghjklzxcvbnm'
        p1 = 0
        p2 = len(s)-1
        s2 = s.lower()
        while p1 < p2:
            c1 = s2[p1]
            c2 = s2[p2] 
            if c1 in alpha_num:
                if c2 in alpha_num:
                    if c1 != c2:
                        return False
                    p1 += 1
                p2 -= 1
            elif c2 in alpha_num:
                p1 += 1
            else:
                p1 += 1
                p2 -= 1
        return True
   
    '''
    def isPalindrome(self, s: str) -> bool:
        Solution #1: Stack
        alpha_num = '1234567890qwertyuiopasdfghjklzxcvbnm'
        s2 = ''
        for char in s.lower():
            if char in alpha_num:
                s2 += char
        half_len = int(len(s2)/2)
        if half_len == 0:
            return True
        stack = []
        for char in s2[:half_len]:
            stack += char
        for char in s2[-half_len:len(s2)]:
            if stack.pop() != char:
                return False
        return True
    '''