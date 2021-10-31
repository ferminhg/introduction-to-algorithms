package main

import "fmt"

type node struct {
	next  *node
	value int
}

type linkedList struct {
	head   *node
	tail   *node
	length int
}

func (l *linkedList) add(value int) bool {
	newNode := &node{value: value}
	l.length++
	if l.head == nil {
		l.head = newNode
		l.tail = newNode
		return true
	}

	l.tail.next = newNode
	l.tail = newNode
	return true
}

func (l *linkedList) remove(value int) bool {
	if l.head == nil {
		return false
	}

	if l.head.value == value {
		l.head = l.head.next
		l.length--
		return true
	}

	current := l.head
	for current.next != nil {
		if current.next.value == value {
			current.next = current.next.next
			l.length--
			return true
		}
		current = current.next
	}
	return false
}

func main() {
	list := new(linkedList)
	list.add(1)
	list.add(2)
	list.add(3)
	fmt.Println(list)

	list.remove(2)
	list.remove(3)
	fmt.Println(list)
}
