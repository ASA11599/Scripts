package main

import (
	"fmt"
	"strings"
)

type DocumentStore struct {
	docs  []string
	index map[string][]int
}

func NewDocumentStore() *DocumentStore {
	return &DocumentStore{
		docs:  make([]string, 0),
		index: make(map[string][]int),
	}
}

func (ds *DocumentStore) Add(doc string) {
	// Insert the document
	ds.docs = append(ds.docs, doc)
	docIndex := len(ds.docs) - 1
	// Update the index
	words := strings.Split(doc, " ")
	for _, w := range words {
		if ds.index[w] == nil {
			ds.index[w] = make([]int, 0, 1)
		}
		ds.index[w] = append(ds.index[w], docIndex)
	}
}

func (ds *DocumentStore) Search(word string) []string {
	docs := make([]string, 0)
	if ds.index[word] != nil {
		for _, di := range ds.index[word] {
			docs = append(docs, ds.docs[di])
		}
	}
	return docs
}

func main() {
	docStore := NewDocumentStore()
	docStore.Add("This site uses cookies")
	docStore.Add("A sentence that contains 6 words")
	docStore.Add("The monster ate all the cookies")
	docStore.Add("I ate my homework")
	fmt.Println(docStore.Search("cookies"))
	fmt.Println(docStore.Search("ate"))
	fmt.Println(docStore.Search("homework"))
	fmt.Println(docStore.Search("sentence"))
}
