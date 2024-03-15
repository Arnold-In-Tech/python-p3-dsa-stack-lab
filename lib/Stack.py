class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
            return False if len(self.items) != 0 else True 

    def push(self, item):
        if not self.full():        
            return self.items.insert(len(self.items), item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()		

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)
        
    def full(self):
        return True if len(self.items) >= self.limit else False

    def search(self, target):
        return (len(self.items) - 1) - self.items.index(target) if target in self.items else -1
