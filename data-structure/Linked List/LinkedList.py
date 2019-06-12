class ListNode:
    def __init__(self, val, next, *args, **kwargs):
        self.val = val
        self.next = None
        # return super().__init__(*args, **kwargs)
        
        def reverse(self, head):
            prev = None
            
            while head:
                temp = head.next
                head.next = prev
                
                prev = head
                head = temp
            return prev

class DListNode:
    def __init__(self, val, next, prev, *args, **kwargs):
        self.val = val
        self.next = None
        self.prev = None
        
        def reverse(self, head):
            curt = None
            while head:
                curt = head
                head = curt.next
                
                curt.next = curt.prev
                curt.prev = curt
            return curt
            pass
     
                
                
            


