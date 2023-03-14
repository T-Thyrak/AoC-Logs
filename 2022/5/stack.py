class Stack:
    def __init__(self, items: list = None):
        self._items = items.copy() if items else []
        
    def push(self, item):
        self._items.append(item)
        
    def pop(self, count: int = 1):
        if count == 1:
            return self._items.pop()
        else:
            return [self._items.pop() for i in range(count)]
        
    def push_all(self, items):
        for item in items:
            self.push(item)
            
    def move(self, count: int, target: 'Stack', retain_order=False):
        if retain_order:
            items = self.pop(count)
            if count > 1:
                items.reverse()
            target.push_all(items)
        else:
            target.push_all(self.pop(count))
        
    def reverse(self):
        if len(self._items) > 1:
            self._items.reverse()
        
    def peek(self):
        return self._items[-1]
    
    def __repr__(self):
        return f"Stack(items={self._items})"