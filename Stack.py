class Stack:
    def __init__(self):
        self.item=[]
    def push(self,item):
        return self.item.append(item)
    def pop(self):
        return self.item.pop()
    def is_empty(self):
        if self.item==[]:
            return True
        return False
    def show(self):
        return self.item
    
if __name__ =="__main__":
    s=Stack()
    s.push(3)
    s.push(5)
    s.push(6)
    print(s.show())
        
