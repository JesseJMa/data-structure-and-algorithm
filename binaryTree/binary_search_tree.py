#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, Optional
import math

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    """
    1) 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
    2) 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
    3) 任意节点的左、右子树也分别为二叉查找树；
    4) 没有键值相等的节点。
    """
    
    
    def __init__(self, val_list: List[int]):
        self.root = None
        for n in val_list:
            self.insert(n)
            
    def insert(self, data: int):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            n = self.root
            while n:
                p = n
                
                if n.val > data:
                    n = n.left
                else:
                    n = n.right
            new_node = TreeNode(data)
            new_node.parent = p
            
            if p.val > data:
                p.left = new_node
            else:
                p.right = new_node
        return True
    
    def search(self, data) -> Optional[List[TreeNode]]:
        if self.root is None:
            return False
        else:
            result = []
            n = self.root
            while n:
                if n.val == data:
                    result.append(n)
                elif data < n.val:
                    n = n.left 
                else:
                    n = n.right
        return result
    
    def delMin(self, node):
        if node.left is None:
            return node
        else:
            while node:
                node = node.left
        return node
                
    def _bst_min_node(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:   # 找到左子树的头
            return subtree
        else:
            return self._bst_min_node(subtree.left)             
    
    def remove(self, root, data):
        return self._bst_remove(root, data)
     
    def _bst_remove(self, subtree, data):
        """remove target node and return root"""
        if subtree is None:
            return None
        elif data < subtree.val:
            subtree.left = self._bst_remove(subtree.left, data)
            return subtree
        elif data > subtree.val:
            subtree.right = self._bst_remove(subtree.right, data)
            return subtree
        else: # find the target node 
            if subtree.left is None and subtree.right is None:
                return None  # has no child, make its the pointer from its parent to it node
            
            elif subtree.left is None or subtree.right is not None: # only has one child
                if subtree.left is not None:
                    return subtree._left
                else:
                    return subtree.right
            else:  # has two children
                # find its successor and delete its successor = min(subtree -> right)
                successor_node = self._bst_min_node(subtree.right)
                subtree.val = successor_node.val
                subtree.right = self._bst_remove(successor_node, data)
                return subtree
    # def _bfs(self):
        
    #     if self.root is None:
    #         return []

    #     ret = []
    #     q = Queue()
    #     # 队列[节点，编号]
    #     q.put((self.root, 1))

    #     while not q.empty():
    #         n = q.get()

    #         if n[0] is not None:
    #             ret.append((n[0].val, n[1]))
    #             q.put((n[0].left, n[1]*2))
    #             q.put((n[0].right, n[1]*2+1))

    #     return ret
              
                
    def __repr__(self):
            # return str(self.in_order())
        # print(str(self.in_order()))
        return self._draw_tree()         
                
    def _draw_tree(self):
        """
        可视化
        :return:
        """
        nodes = self._bfs()
        
        if not nodes:
            print('This tree has no nodes.')
            return

        layer_num = int(math.log(nodes[-1][1], 2)) + 1
        
        prt_nums = []
        
        for i in range(layer_num):
            prt_nums.append([None]*2**i)

        for v, p in nodes:
            row = int(math.log(p ,2))
            col = p % 2**row
            prt_nums[row][col] = v

        prt_str = ''
        for l in prt_nums:
            prt_str += str(l)[1:-1] + '\n'

        return prt_str            
                
            
nums = [4, 2, 5, 6, 1, 7, 3]
bst = BinarySearchTree(nums)
print(bst)   
            
                
           


        