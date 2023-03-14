from __future__ import annotations
from typing import Callable

class Tree:
    def __init__(self, data: str = None, parent: Tree = None, depth: int = 0) -> None:
        self.data = data
        self.children = []
        self.parent = parent
        self.depth = depth
        
    def add_child(self, child: str) -> Tree:
        tree = Tree(child, self, self.depth + 1)
        self.children.append(tree)
        
        return tree
        
    def get_parent(self) -> Tree:
        return self.parent
    
    def walk(self, callback: Callable[[Tree], None]) -> None:
        callback(self)
        
        for child in self.children:
            child.walk(callback)