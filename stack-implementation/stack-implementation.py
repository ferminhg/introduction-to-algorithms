class Element:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self):
        return 'data => ' + str(self.data) + '\n next => ' + str(self.next)

class FIFOList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, item):
        item.next = self.head
        self.head = item
        self.size =+ 1
        return True

    def pop(self):
        if self.head is None:
            return False
        item = Element(self.head.data)
        self.head = self.head.next
        return item

    @classmethod
    def createList(cls):
        return FIFOList()


fifo = FIFOList.createList()
fifo.push(Element(1))
fifo.push(Element(2))
print(fifo.head)
element = fifo.pop()
print(element)
element = fifo.pop()
print(element)
