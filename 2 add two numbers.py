# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return_list = ListNode()
        head = return_list
        carry = 0
        while l1 or l2 or carry:
            current_sum = 0
            if l1: 
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val
                l2 = l2.next
                
            current_sum += carry
            digit = current_sum % 10
            carry = current_sum // 10
            return_list.next = ListNode(digit)
            return_list = return_list.next
        return head.next
            
        
        """
        list1 = [2,4,3], List2 = [5,6,4]
            
        ---------
            1(carry)
            2 4 3
           +5 6 4
        ----------
        Ans 8 0 7
        ---------
        """
        