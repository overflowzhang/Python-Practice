
class Stack(object):
    def __init__(self):
        self.data_stack = []

    def init_stack(self):
        self.data_stack = []

    def insert(self,data):
        self.data_stack.append(data)

    def pop(self):
        if len(self.data_stack)==0:
            return None
        data = self.data_stack[-1]
        del self.data_stack[-1]
        return data

    def size(self):
        return len(self.data_stack)


stack = Stack()
stack.insert(1)
stack.insert(2)
stack.insert(3)
print("The size of stack : ")
print(stack.size())
print('The stack is : ')
print(stack)
for i in range(1,stack.size()+1):
    tail = stack.pop()
    print(tail)

