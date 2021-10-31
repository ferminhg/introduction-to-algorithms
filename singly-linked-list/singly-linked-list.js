class Node {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

class SinglyLinkedList {
    constructor() {
        this.head = null
        this.tail = null
        this.size = 0
    }

    add(node) {
        if (!this.head) {
            return this.insertWhenListEmpty(node)
        }

        this.size++
        this.tail.next = node
        this.tail = node
        return true
    }

    insertWhenListEmpty(node) {
        this.size++
        this.head = node
        this.tail = node
        return true
    }

    find(data) {
        let current = this.head

        while (current != null && current.data != data) {
            current = current.next
        }

        if (current == null) {
            return false
        }
        return current
    }

    delete(data) {
        if (this.head == null)
            return false
        if (this.head.value == data) {
            this.head = this.head.next
            this.size--
            return true
        }

        let current = this.head
        while (current.next != null && current.next.value != data) {
            current = current.next
        }

        if (current.next == null){
            return false
        }

        current.next = current.next.next
        this.size--
        return true
    }
}


list = new SinglyLinkedList()
list.add(new Node(1))
list.add(new Node(2))
list.add(new Node(3))
console.log(list.head)
console.log(list.size)

list.delete(2)
console.log(list.head)
