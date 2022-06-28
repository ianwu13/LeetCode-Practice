'''
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # Dictionary is a hashmap
        for i, val in enumerate(nums):
            if target-val in hashmap:
                return [i, hashmap[target-val]]
            hashmap[val] = i

    '''
    # Brute Force
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val1 in enumerate(nums):
            if val1 <= target:
                for j, val2 in enumerate(nums[i+1:]):
                    if val1+val2:
                        return [i, j+i+1]
    '''