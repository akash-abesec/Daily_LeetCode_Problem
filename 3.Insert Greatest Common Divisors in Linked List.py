# Problem :- https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/?envType=daily-question&envId=2024-09-10

# Solution :- https://www.youtube.com/watch?v=XW65h7W1K20&ab_channel=PrakharAgrawal

# 2807. Insert Greatest Common Divisors in Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(a, b):
        if a==0:
            return b
        return self.gcd(b%a, a)
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head.val
        temp = head
        while(temp.next != None):
            curr = temp.next.val
            node = ListNode(gcd(curr, prev))
            node.next = temp.next
            temp.next = node
            prev = curr
            temp = temp.next.next
        return head
