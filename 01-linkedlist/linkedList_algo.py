"""
1) Reverse single-linked-list
2) Detect cycle
3) Merge two sorted linked list
4) Remove nth node from the end
5) find the middle node

Author: JesseJMa
"""

from typing import Optional

class Node:
    def __init__(self, data: int, next: None):
        self.data = data
        self._next = next
        
        
# Reverse single-linked list
def reverse(head: Node) -> Optional[Node]:
    current = head
    reversed_head = None
    
    while current:
        reversed_head, reversed_head._next, current = current, reversed_head, current._next
    return reversed_head

# Detect cycle in a single linked-list
def has_cycle(head: Node) -> bool:
    slow, fast = head, head
    
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
        if slow == fast:
            return True
    return False

# Merge two sorted linked list
def merge_sorted_linked_list(l1: Node, l2: Node) -> Optional[Node]:
    result = Node(None)
    head = result
    
    while l1 and l2:
        if l1.data < l2.data:
            result._next = l1
            l1 = l1._next
        if l1.data >= l2.data:
            result._next = l2
            l2 = l2._next
        result = result._next
    if l1:
        result._next = l1
    if l2:
        result._next = l2
        
    return head._next

# Remove nth node from the end
def remove_nth_from_end(head: Node, n: int) -> Optional[Node]:
    # double pointer fast 
    
    fast = head
    count = 0
    
    while fast and count < n:
        fast = fast._next
        count += 1
    if not fast and count < n:
        return head
    if not fast and count == n:
        return head._next
    
    slow = head
    while fast._next:
        fast, slow = fast._next, slow._next
    slow._next = slow._next._next
    
    return head

# find middle node
def find_middle_node(head: Node) -> Optional[Node]:
    # fast = head
    # count = 0
    # while fast:
    #     fast = fast._next
    #     count += 1
    # middle = count // 2
    # if middle % 2 == 0:
    #     return None
    # slow = head
    # pointer = 0
    # while slow and pointer < middle:
    #     slow = slow._next
    #     point += 1
    
    # return slow 
    
    """
    tow pointers: fast and slow
    """
    
    slow, fast = head
    
    fast = fast._next if fast._next else None
    
    while fast:
        slow, fast = slow._next, fast._next._next
    return slow
        
        
    
    
    def print_all(head: Node):
        nums = []
        current = head
        while current:
            nums.append(current.data)
            current = current._next
        print("->".join(str(num) for num in nums))    
    
   
    
        
    