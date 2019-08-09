#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
implement of Priority Queue base on Heap
"""

import math

class QueueNode:
    def __init__(self, priority, data=None):
        assert type(priority) is int and priority >= 0
        self.data = data
        self.priority = priority
        
class PriorityQueue:
    def __init__(self, capacity=100):
        self._q = []
        self._capacity = capacity
        self._length = 0
        
    def enqueue(self, data, priority):
        if self._length > self._capacity:
            return False
        
        newNode = QueueNode(priority, data)
        self._q.append(newNode)
        self._length += 1
        
        
        
        nn = self._length - 1
        
        while nn > 0:
            lp = nn // 2  # the last Parent node index
            
            if self._q[nn].priority > self._q[lp].priority:
                self._q[nn], self._q[lp] = self._q[lp],  self._q[nn]
                nn = lp
            else:
                break
        return True
            
        
            
        
        
        
        
       
        
        

