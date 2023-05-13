class Iterator:
    def __init__(self):
        
        return self
    
    def __iter__(self, x):
        self.x = 2
        return self
    
    def __next__(self):
        x = x.self
        x += 1
        if x > 15:
            raise StopIteration
        return x
    
iterator = Iterator()
print(iterator)