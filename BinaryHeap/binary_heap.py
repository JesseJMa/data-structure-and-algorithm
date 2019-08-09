#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import random

"""
Max Heap
"""

class BinaryHeap:
    def __init__(self, data=None, capacity=100):
        self._data = []
        self._capacity = capacity
        
        if type(data) is list:
            if len(self._data) > self._capacity:
                raise Exception('Heap oversize, capacity:{}, data size:{}'.format(self._capacity, len(data)))
            self._type_assert(data)
            
            self._data = data
        self._length = len(self._data)
        
        
    def heapify(self):
        """
        堆化
        """
        
        self._heapify(self._data, self._length - 1)
        
    def _heapify(self, data, tail_idx):
        """
        堆化 内部实现
        :param data: 需要堆化的数据
        :param tail_idx: 尾元素是索引
        """
        
        if tail_idx <= 0:
            return 
        lp = (len(data) - 1) // 2
        
        for i in range(lp, -1, -1):
            self._heap_down(data, i, tail_idx)
    
    
    
    @staticmethod  
    def _heap_down(data, idx, tail_idx):
        """
        在指定位置  堆化操作
        :param idx: data 中需要执行 堆化的位置
        :param tail_idx: 尾元素的  索引
        :return:
        """
        
        assert type(data) is list
        
        lp = (tail_idx - 1) // 2
        
        while idx <= lp:
            
            lc = idx * 2 + 1
            rc = lc + 1
            
            if rc <= tail_idx:
                tmp = rc if data[lc] < data[rc] else lc
            else:
                tmp = lc
            if data[lp] < data[tmp]:
                data[lp], data[tmp] = data[tmp], data[lp]
                idx = tmp
            else:
                break
    
    def insert(self, num):
        if self._length < self._capacity:
            if self._insert(self._data, num):
                self._length += 1
                return True
        return False
    
    @staticmethod
    def _insert(data, num)      :
        """
        堆中插入元素的内部实现
        :param data:
        :param num:
        :return:
        """
        
        assert type(data) is list
        assert type(num) is int
        
        data.append(num)
        length = len(data)
        
        nn = length - 1
        
        while nn > 0:
            p = (nn - 1) // 2 # Parent index
            if data[nn] > data[p]:
                data[p], data[nn] = data[nn], data[p]
                nn = p
            else:
                break
        return True
    
    def get_top(self):
        """
        取堆顶
        :return:
        """
        if self._length <= 0:
            return None
        return self._data[0]
    
    def remove_top(self):
        """
        取堆顶，并返回剩余的结构
        :return:
        """
        ret = None
        if self._length > 0:
            ret = self._remove_top(self._data)
            self._length -= 1
        return ret
    @staticmethod
    def _remove_top(data):
        """
        取堆顶 内部实现
        :param data:
        :return:
        """
        assert type(data) is list
        
        length = len(data)
        if length == 0:
            return None
        
        data[0], data[-1] = data[-1], data[0] # last element replace top 
        
        # shift down
        ret = data.pop()
        
        length -= 1
        
        if length > 1:
            BinaryHeap._heap_down(data, 0, length - 1)
        return ret
    
    @staticmethod
    def _type_assert(nums):
        assert type(nums) is list
        
        for n in nums:
            assert type(n) is int
            
    @staticmethod
    def _draw_heap(data):
        """
        格式化打印
        :param data:
        :return:
        """
        
        length = len(data)
        
        if length == 0:
            return "empty heap"
        ret = ''
        
        for i, n in enumerate(data):
            ret += str(n)
            
            # 每行最后一个换行
            if i == 2 ** int(math.log(i + 1, 2) + 1) - 2 or i == len(data) - 1:
                ret += '\n'
            else:
                ret += ', '
        return ret
    
        
        
        
        
        
         
                
        
        
        
        
        
        
        
        
        