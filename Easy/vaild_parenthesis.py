'''
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        openers = {'{', '[', '('}
        matcher = {'}':'{', ']':'[', ')':'('}
        stack = []
        for char in str(s):
            if char in openers:
                stack.append(char)
            elif len(stack) == 0 or stack.pop() != matcher[char]:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        