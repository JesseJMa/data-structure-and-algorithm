"""
1) Insertion, delete, search of single-linked list
2) Assume int type for data in list nodes

Author: JesseJMa
"""

from typing import Optional

class Node:
    def __init__(self, data: int, next_node: None):
        self.data = data
        self._next = next_node