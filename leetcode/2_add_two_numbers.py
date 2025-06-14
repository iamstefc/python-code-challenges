from typing import Optional
'''
You are given two non-empty linked lists representing two non-negative integers. 

The digits are stored in reverse order, and each of their nodes contains a single digit. 

Add the two numbers and return the sum as a linked list.
'''
# singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy head node, first node.
        # point start of list at current
        dummy_head = ListNode(0)
        current = dummy_head
        
        # store carry-overs from addition like 18 take the 1
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            # add two numbers for new node, get remainder for carry
            total_sum = val1 + val2 + carry
            new_digit = total_sum % 10
            carry = total_sum // 10

            # add new_digit to start of linked list, move pointer for next new_digit
            current.next = ListNode(new_digit)
            current = current.next

            # if list not empty on next iteration
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # result from loop goes all into the dummy list for final output
        return dummy_head.next

def create_linked_list(arr: list) -> Optional[ListNode]:
    '''
    convert a Python list into a ListNode linked list
    '''
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def print_linked_list(head: Optional[ListNode]) -> list:
    '''
    convert a ListNode linked list back to a Python list
    '''
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":

    py_list1 = [2, 4, 3]
    py_list2 = [5, 6, 4]
    
    l1_node = create_linked_list(py_list1)
    l2_node = create_linked_list(py_list2)

    solution = Solution()
    sum_list_node = solution.addTwoNumbers(l1_node, l2_node)
    print(print_linked_list(sum_list_node)) # output [7,0,8]