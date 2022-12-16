class ListNode(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            
            curr = temp
        
        return prev
    
# create listnode
n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

ans = Solution()
t1 = ans.reverseList(n1)

print(t1.val, t1.next.val)

