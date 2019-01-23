
class Queue(object):
    def __init__(self,a):
        self.data_list =  a

    def in_queue(self,data):
        self.data_list.append(data)

    def out_queue(self):
        if len(self.data_list) == 0:
            return None
        data = self.data_list[0]
        del self.data_list[0]
        return data

    def size(self):
        return len(self.data_list)


a = []
for i in range(0,10):
    a.append(i)
queue = Queue(a)
queue.in_queue(11)
queue.in_queue(12)
queue.in_queue(13)
head = queue.out_queue()
print(head)
print(queue.size())