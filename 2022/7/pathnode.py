from __future__ import annotations

from path import Path
from typing import Callable

class PathNode:
    def __init__(self, name=None, parent=None):
        self._name = name
        self._size = 0
        self._parent = parent
        self._children = []
        
    def is_file(self):
        return len(self._children) == 0
    
    def add_child(self, child: PathNode):
        self._children.append(child)
        
    def get_child(self, name: str):
        for child in self._children:
            if child._name == name:
                return child
        return None
    
    def goto(self, path: Path):
        # print(f"path: {path}")
        # if path is empty, return self
        if len(path._dirs) == 0:
            return self
        
        loc = self
        for name in path._dirs:
            if name == "..":
                if loc._parent is not None:
                    loc = loc._parent
            elif name == ".":
                pass
            else:
                child = loc.get_child(name)
                if child is not None:
                    loc = child
                else:
                    return None
        
        return loc
    
    def get_size(self):
        if self.is_file():
            return self._size
        else:
            size = 0
            for child in self._children:
                size += child.get_size()
            return size
                
    def walk(self, callback: Callable[[PathNode], None]):
        callback(self)
        for child in self._children:
            child.walk(callback)
            
    def __repr__(self):
        return f"<PathNode name={self._name} size={self._size} children={self._children}>"