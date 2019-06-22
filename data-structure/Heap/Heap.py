"""
Max-Heap
Author: JesseJMa
"""

class Heap:
    def __init__(self, capacity: int):
        self._capacity = capacity  # allocate capacity for heap
        self._data = [0] * (capacity + 1) 
        self._count = 0
    
    @classmethod
    def _parent(cls, child_index: int) -> int:
       
        return child_index // 2
    
    @classmethod 
    def _left(cls, parent_index: int) -> int:
        """The left child index."""
        return parent_index * 2 - 1
    
    @classmethod
    def _right(cls, parent_index: int) -> int:
        return parent_index * 2 + 1
    
    def _shiftUp(self) -> None:
        i, parent = self._count, Heap._parent(self._count)
        while parent and self._data[parent] < self._data[i]:
            tmp = self._data[parent]
            self._data[parent] = self._data[i]
            self._data[i] = tmp
            
            i = parent
            parent = Heap._parent(parent)
    
    def _insert(self, value: int) -> None:
        if self._count > self._capacity: return
        self._count += 1
        self._data[self._count] = value
        self._shiftUp()