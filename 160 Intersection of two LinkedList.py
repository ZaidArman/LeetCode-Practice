# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        # Check if either of the linked lists is empty
        if not headA or not headB:
            return None

        # Initialize two pointers, one for each linked list
        pointerA = headA
        pointerB = headB

        # Traverse the linked lists until the intersection is found
        while pointerA != pointerB:
            # If a pointer reaches the end of its linked list, move it to the head of the other list
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # Return the intersection node (or None if there is no intersection)
        return pointerA
