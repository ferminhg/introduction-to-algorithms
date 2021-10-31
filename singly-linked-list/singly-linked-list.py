class NodeNotFoundException(Exception):
    pass
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __str__(self):
        return 'data => ' + str(self.data) + '\n next => ' + str(self.next)
class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.size = 0

    def add(self, node: Node) -> bool:
        if self.__head is None:
            return self.__insertWhenListEmpty(node)

        self.size += 1
        self.__tail.next = node
        self.__tail = node
        return True

    def insertInFront(self, node: Node) -> bool:
        if self.__head is None:
            return self.__insertWhenListEmpty(node)

        self.size += 1
        node.next = self.__head
        self.__head = node
        return True

    def __insertWhenListEmpty(self, node:Node) -> bool:
        self.size += 1
        self.__head = node
        self.__tail = node
        return True

    def find(self, data: int) -> Node:
        current = self.__head
        while current is not None and current.data != data:
            current = current.next

        if current is None:
            raise NodeNotFoundException(data)
        return current

    def delete(self, data: int) -> bool:
        if self.__head is None:
            return False

        if self.__head.data == data:
            self.__head = self.__head.next
            self.size -= 1
            return True

        current = self.__head
        while current.next is not None and current.next.data != data:
            current = current.next

        if current.next is None:
            return False

        current.next = current.next.next
        self.size -= 1
        return True

    def head(self) -> Node:
        return self.__head

    def __str__(self):
        return self.__head


list = SinglyLinkedList()
list.add(Node(1))
list.add(Node(2))
list.add(Node(3))
print(list.head())
print(list.size)

print(list.find(2))
# print(list.find(4))
print(list.delete(2))
print(list.head())
