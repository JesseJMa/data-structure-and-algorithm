#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Author: JesseJMa
Contact: jessejiema@tencent.com

"""

"""
Binary Heap
Max Heap
Min Heap

"""

from typing import Optional
import math
import random

class Heap:
    def __init__(self, capacity = 100, nums = None):
        self._data = []
        self._capacity = capacity
        
        # print(nums)
        
        if type(nums) == list and len(nums) < self._capacity:
            for n in nums:
                assert type(n) is int
                self._data.append(n)
                
            self._length = len(self._data)
            self._heapify()
            
    def _heapify(self):
        if self._length <= 1:
            return
        lp = (self._length - 2) // 2
        
        for i in range(lp, -1, -1):
            self._heap_down(i)
    
    def _heap_down(self, idx):
        pass
    
    def insert(self, num):
        pass
    def get_top(self):
        if self._length <= 0:
            return None
        return self._data[0]
    
    def remove_top(self):
        if self._length <= 0:
            return None
        
        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        ret = self._data.pop()
        self._length -= 1
        
        self._head_down(0)
        
        return ret
    
    def get_data(self):
        return self._data
    def get_length(self):
        return self._length
    
    @staticmethod
    def _draw_heap(data):
        length = len(data)
        if length <= 0:
            return 'empty heap'
        ret = ''
        for idx, val in enumerate(data):
            ret += str(val)
            if idx == 2 ** int(math.log(idx + 1, 2) + 1) - 2 or idx == len(data) - 1:
                ret += '\n'
            else:
                ret += ', '
        return ret
    
    def __repr__(self):
        print(self._data)
        return self._draw_heap(self._data)

class MaxHeap(Heap):
    
    def __heap_down(self, idx):
        if self._length <= 1:
            return 
        lp = (self._length - 2) // 2   # last Parent Node index
        
        while idx <= lp:
            lc = idx * 2 + 1
            rc = lc + 1
            
            if rc <= self._length - 1:
                tmp = lc if self._data[lc] > self._data[idx] else rc
            else:
                tmp = lc
            
            if self._data[tmp] > self._data[idx]:
                self._data[tmp], self._data[idx] = self._data[idx], self._data[tmp]
                idx = tmp
            else:
                break
        
    def insert(self, num):
        if self._length <= self._capacity:
            return False
        self._data.append(num)
        self._length += 1
        
        nn = self._length - 1
        while nn >0:
            p = (nn - 1) // 2
            
            if self._data[nn] > self._data[p]:
                self._data[nn], self._data[p] = self._data[p], self._data[nn]
                nn = p
            else:
                break
        return True
            
            
            
            
            
            
            
            



if __name__ == '__main__':
    nums = list(range(10))
    random.shuffle(nums)
    print('--', nums)
    
    max_h = MaxHeap(100, nums)
    print('---- max heap ----')
    print(max_h)
    pass
  