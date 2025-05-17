class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev,curr ,next. three vars
        prev = None # head tail
        curr = head # 1
        while curr:
            next_node = curr.next
            curr.next = prev  
            prev = curr 
            curr = next_node
        return prev
