from __future__ import annotations

from pathnode import PathNode
from path import Path

from typing import Callable

class PathTree:
    def __init__(self):
        self._root = PathNode("/")
        self._cwd = Path()
        
    def cd(self, path: str):
        # print(f"cd path: {path}")
        self._cwd.cd(path)
        
    def add_dir(self, dirname: str):
        loc = self._root.goto(self._cwd)
        # print(f"loc: {loc}")
        if loc is not None:
            loc.add_child(PathNode(name=dirname, parent=loc))
            
    def add_file(self, filename: str, size: int):
        loc = self._root.goto(self._cwd)
        if loc is not None:
            child = PathNode(name=filename, parent=loc)
            child._size = size
            
            loc.add_child(child)
            
    def walk(self, callback: Callable[[PathNode], None]):
        self._root.walk(callback)