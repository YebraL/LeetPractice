"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
       
        part1 = []
        part2 = []
        
        while l1.next != None:
            part1.append(l1.val)
            if l1.next.next == None:
                part1.append(l1.next.val)
            l1 = l1.next
            
        while l2.next != None:
            part2.append(l2.val)
            if l2.next.next == None:
                part2.append(l2.next.val)
            l2 = l2.next
            
        str1 = ''.join(map(str,part1))
        str2 = ''.join(map(str,part2))
        sum_total = int(str1) + int(str2)
        
        if sum_total == 0:
            node_zero = ListNode(0)
            return node_zero
        
        sum_string = str(sum_total)[::-1]
        # print(sum_string[1:])
        node_result = ListNode(int(sum_string[0]))
        for i in sum_string[1:]:
            node1 = ListNode(int(i))
            node_result.next = node1
            
        return node_result

m1 = ListNode(3)
m2 = ListNode(4, m1)
m3 = ListNode(2, m2)

n1 = ListNode(4)
n2 = ListNode(6, n1)
n3 = ListNode(5, n2)


# while m3.next != None:
#     print(m3.val)
#     if m3.next.next == None:
#         print(m3.next.val)    
#     m3 = m3.next
        
test = Solution()
test.addTwoNumbers(m3, n3)
    