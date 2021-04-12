# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# method1: stack + dummpy point(哑结点)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummpy = ListNode(-1, head)
        stack = []
        pointer = dummpy
        while pointer is not None:
            stack.append(pointer)
            pointer = pointer.next
        stack[-n-1].next = stack[-n].next
        return dummpy.next

# method2: double pointer(fast pointer, slow pointer)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummpy = ListNode(-1, head)
        fast, slow = head, dummpy
        for _ in range(n):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummpy.next