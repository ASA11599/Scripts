package main

import (
	"errors"
	"fmt"
)

type List[T any] interface {
	Size() int
	Get(index int) (T, error)
	Insert(index int, value T) error
	Remove(index int) error
}

type LinkedListNode[T any] struct {
	value T
	next  *LinkedListNode[T]
}

func (this *LinkedListNode[T]) GetValue() T {
	return this.value
}

func (this *LinkedListNode[T]) GetNext() *LinkedListNode[T] {
	return this.next
}

type LinkedList[T any] struct {
	size int
	head *LinkedListNode[T]
}

func (this *LinkedList[T]) Size() int {
	return this.size
}

func (this *LinkedList[T]) Get(index int) (T, error) {
	var v T
	if index >= this.Size() {
		return v, errors.New(fmt.Sprintf("Error getting index %d: list size is %d", index, this.Size()))
	}
	current := this.head
	i := 0
	for i != index {
		current = current.GetNext()
		i++
	}
	v = current.GetValue()
	return v, nil
}

func (this *LinkedList[T]) Insert(index int, value T) error {
	if (index <= this.Size()) || (index == 0 && this.Size() == 0) {
		if this.Size() == 0 {
			this.head = &LinkedListNode[T]{value, nil}
		} else {
			if index == 0 {
				this.head = &LinkedListNode[T]{value, this.head}
			} else {
				current := this.head
				i := 0
				for i != (index - 1) {
					current = current.GetNext()
					i++
				}
				current.next = &LinkedListNode[T]{value, current.next}
			}
		}
		this.size++
		return nil
	} else {
		return errors.New(fmt.Sprintf("Error inserting at index %d: list size is %d", index, this.Size()))
	}
}

func (this *LinkedList[T]) Remove(index int) error {
	if (index < this.Size()) && (this.Size() > 0) {
		if this.Size() == 1 {
			this.head = nil
			this.size--
		} else {
			current := this.head
			i := 0
			for i != (index - 1) {
				current = current.GetNext()
				i++
			}
			current.next = current.GetNext().GetNext()
		}
		this.size--
		return nil
	} else {
		return errors.New(fmt.Sprintf("Error removing from index %d: list size is %d", index, this.Size()))
	}
}

func (this *LinkedList[T]) String() string {
	res := ""
	current := this.head
	for current != nil {
		res += fmt.Sprintf("%+v", current.GetValue())
		if current.GetNext() != nil {
			res += " -> "
		}
		current = current.GetNext()
	}
	return fmt.Sprintf("LinkedList{%s}", res)
}

func (this *LinkedList[T]) Append(value T) {
	this.Insert(this.Size(), value)
}

func (this *LinkedList[T]) Pop() {
	this.Remove(this.Size() - 1)
}

func main() {
	var list List[int] = &LinkedList[int]{}
	fmt.Println(list)
	list.(*LinkedList[int]).Append(56)
	fmt.Println(list)
	list.(*LinkedList[int]).Append(57)
	fmt.Println(list)
	list.(*LinkedList[int]).Append(58)
	fmt.Println(list)
	list.(*LinkedList[int]).Append(59)
	fmt.Println(list)
	list.(*LinkedList[int]).Pop()
	fmt.Println(list)
	list.(*LinkedList[int]).Pop()
	fmt.Println(list)
	list.(*LinkedList[int]).Pop()
	fmt.Println(list)
	list.(*LinkedList[int]).Pop()
	fmt.Println(list)
}
