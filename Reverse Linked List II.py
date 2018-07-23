### leetcode 92; EPI 7.2
### following code beats 97.90% python3 submissions as of july22,2018 

class ListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node
        
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = sub_head = ListNode(0,head)
        for _ in range(1,m):
            sub_head = sub_head.next

        sub_iter = sub_head.next
        for _ in range(n - m):
            temp = sub_iter.next
            sub_iter.next, temp.next, sub_head.next = (temp.next, sub_head.next, temp)
        return dummy.next
# time complexity is O(n), n is the number of elements in the linkedlist
# space complexity is O(1), constant
