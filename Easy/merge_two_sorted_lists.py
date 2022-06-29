'''
https://leetcode.com/problems/merge-two-sorted-lists/

DIDN'T LOVE THIS PROBLEM, JUST SOLVED WITH THREE POINTER, DOESNT SEEM TO BE OPTIMIZABLE FURTHER THROUGH DATASTRUCTURES

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val > list2.val:
            tmp = list2
            list2 = list1
            list1 = tmp
        start = list1
        
        tmp = ListNode(next=list1)
        while list2 != None and list1 != None:
            if list2.val < list1.val:
                tmp.next = list2
                tmp = list2
                list2 = tmp.next
                tmp.next = list1
            else:
                tmp = list1
                list1 = list1.next
                
        # Add remaining list2 elements if necessary
        if list2 != None:
            tmp.next = list2
            
        return start
    