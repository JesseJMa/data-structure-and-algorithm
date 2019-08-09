#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
binary search tree
"""
class BSTNode(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right


class BST(object):
    def __init__(self, root=None):
        self.root = root
        
    @classmethod
    def draw_from(cls, node_list):
        cls.size = 0
        key_to_node_dict = {}
        
        for node_dict in node_list:
            key = node_dict['key']
            key_to_node_dict[key] = BSTNode(key, value=key)
            
        for node_dict in node_list:
            key = node_dict['key']
            node = key_to_node_dict[key]
            
            if node_dict['is_root']:
                root = node
            
            node.left = key_to_node_dict.get(node_dict['left'])
            node.right = key_to_node_dict.get(node_dict['right'])
            
            cls.size += 1
            
        return cls(root)
    
    
    def _bst_search(self, subtree, key):
        if subtree is None:
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree
        
    def __contain__(self, key): # get key in the tree if it has, like in opertation
        return self._bst_search(self.root, key) is not None
    
            
    def get(self, key, default=None):   # get the corresponding value of the node with key of key
        target_node = self._bst_search(key)
        if target_node is not None:
            return target_node.value
        return default
    
    
    def _bst_min_node(self, subtree): # the node with the smallest value
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bst_min_node(subtree.left)
  
             
        
            
            
        