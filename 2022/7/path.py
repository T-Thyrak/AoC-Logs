from __future__ import annotations


class Path:
    def __init__(self, path=None):
        self._dirs = []
        
        if path is not None:
            paths = path.split("/")
            if paths[0] == "":
                self._dirs.extend(paths[1:])
                
    def cd(self, path: str):
        if path == ".":
            return
        elif path == "..":
            if len(self._dirs) > 0:
                self._dirs.pop()
        elif path == "/":
            self._dirs = []
        elif path.startswith("/"):
            self._dirs = path.split("/")[1:]
        else:
            self._dirs.extend(path.split("/"))
            
    def __repr__(self):
        return "/" + "/".join(self._dirs)