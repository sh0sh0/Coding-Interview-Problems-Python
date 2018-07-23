### LeetCode 206
### following code beats 99.96% python3 submissions as of july22,2018 

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
# time complexity is O(n), n is the number of elements in the linkedlist
# space complexity is O(1)
