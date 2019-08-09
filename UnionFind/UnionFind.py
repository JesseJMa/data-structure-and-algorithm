#!/usr/bin/python
# -*- coding: UTF-8 -*-

class UnionFind:
    def __init__(self, n):
        self.count = n
        self.id = [0] * n
        for i in range(n):
            self.id[i] = i
            
    def find(self, k):
        assert k >= 0 and k < self.count
        return self.id[k]
    
    def isConnected(self, p, q):
        return self.find(p) == self.find(q)
    
    
    def union(self, p, q):
        self.id[p] = q
    
unionFind = UnionFind(5)

print(unionFind.find(3))

print(unionFind.isConnected(4, 4))

