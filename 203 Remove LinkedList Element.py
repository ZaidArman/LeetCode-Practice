# 203. Remove Linked List Elements
"""
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

# Example 2:
Input: head = [], val = 1
Output: []

# Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

# Constraints:
The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""


# Solution 1: Recursive Approach
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        # Base case: If the head is None, return None (end of the list)
        if not head:
            return head
        # Recursively check the next nodes
        head.next = self.removeElements(head.next, val)
        # If the current node's value matches 'val', return the next node
        return head if head.val != val else head.next


# Solution 2: Two-Pointer Approach
class Solution(object):
    def removeElements(self, head, val):
        # Create a dummy node as the new head
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head

        while current:
            # If the current node's value matches 'val', skip it
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next
    

# Solution 3: Create a New List
class Solution(object):
    def removeElements(self, head, val):
        # Create a new head and tail for the resulting list
        new_head = ListNode(0)
        new_tail = new_head
        current = head

        while current:
            # If the current node's value does not match 'val', add it to the new list
            if current.val != val:
                new_tail.next = ListNode(current.val)
                new_tail = new_tail.next
            current = current.next

        return new_head.next
    
