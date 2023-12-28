package stack

import (
	"container/list"
	"sync"
)

type Stack[T any] interface {
	Len() int
	Push(T)
	Pop() T
}

type LinkedStack[T any] struct {
	llist *list.List
	lock sync.RWMutex
}

func NewLinkedStack[T any]() *LinkedStack[T] {
	return &LinkedStack[T]{
		llist: list.New(),
	}
}

func (ls *LinkedStack[T]) Len() int {
	ls.lock.RLock()
	defer ls.lock.RUnlock()
	return ls.llist.Len()
}

func (ls *LinkedStack[T]) Push(item T) {
	ls.lock.Lock()
	defer ls.lock.Unlock()
	ls.llist.PushBack(item)
}

func (ls *LinkedStack[T]) Pop() T {
	ls.lock.Lock()
	defer ls.lock.Unlock()
	return ls.llist.Remove(ls.llist.Back()).(T)
}
