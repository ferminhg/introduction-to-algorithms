class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def __str__(self):
        return 'data => ' + str(self.data) + '\n next => ' + str(self.next) + '\n'

class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.size = 0

    def add(self, node: Node):
        self.size += 1
        if self.__head is None:
            self.__head = node
            self.__tail = node
            return True

        self.__tail.next = node
        self.__tail = node
        return True

    def head(self) -> Node | None:
        return self.__head

    def __str__(self):
        return self.__head


list = SinglyLinkedList()
list.add(Node(1))
list.add(Node(2))
list.add(Node(3))
print(list.head())
print(list.size)
