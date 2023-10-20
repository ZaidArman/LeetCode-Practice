# 83. Remove Duplicates from Sorted List
"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

# Example 1:
Input: head = [1,1,2]
Output: [1,2]

# Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

# Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        current = head # Initialize the current node as the head of the linked list

        while current and current.next: # Iterate through the linked list
            if current.val == current.next.val: # Check if the current node's value is the same as the next node's value
                current.next = current.next.next # If they are the same, skip the next node by updating the next pointer
            else:                
                current = current.next # If they are different, move to the next node
        return head # Return the head of the modified linked list
