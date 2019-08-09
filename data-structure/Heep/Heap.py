
"""
Max-Heap

Author: Jie Ma

"""

from typing import Optional, List

class Heap:
    def __init__(self, capacity: int):
        self._data = [0] * (capacity + 1)
        self._capacity = capacity
        self._count = 0
    
    @classmethod
    def _parent(cls, child_index: int) -> int:
        """The parent index."""
        return child_index // 2
    
    @classmethod
    def _left(cls, parent_index: int) -> int:
        """The left child index."""
        return 2 * parent_index
    
    @classmethod
    def _right(cls, parent_index: int) -> int:
        """the right child index."""
        return 2 * parent_index + 1
    
    
  
    def _shiftup(self) -> None:
        i, parent = self._count, Heap._parent(self._count)
        while parent and self._data[i] > self._data[parent]:
            self._data[i], self._data[parent] = self._data[parent], self._data[i]
            i, parent = parent, Heap._parent(parent)
    
    def insert(self, value: int) -> None:
        if self._count > self._capacity:
            return
        self._count += 1
        self._data[self._count] = value
        self._shiftup()
        


if __name__ == "__main__":
    heap = Heap(10)
    heap.insert(1)
    heap.insert(3)
    heap.insert(4)
    heap.insert(8)
    
    print(heap)
    

        