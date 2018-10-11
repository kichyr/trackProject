import pytest
from pathlib import Path
from DBList import Double_Linked_List

class  Test_Double_Linked_List:
    def test_negative(self):
        doubleLinkedList = Double_Linked_List()
        assert((doubleLinkedList.push(None)) == None and doubleLinkedList.len() == 1)

    def test_push_pop(self):
        doubleLinkedList = Double_Linked_List()
        doubleLinkedList.push("sdfsf")
        doubleLinkedList.push(1)
        assert(list([doubleLinkedList.pop(), doubleLinkedList.pop(), doubleLinkedList.pop()]) == [1, "sdfsf", None])

    def test_unshift(self):
        doubleLinkedList = Double_Linked_List()
        doubleLinkedList.push("sdfsf")
        doubleLinkedList.push(1)
        doubleLinkedList.unshift(3)
        assert(list([doubleLinkedList.pop(), doubleLinkedList.pop(), doubleLinkedList.pop()]) == [1, "sdfsf", 3])
    
    def test_unshift(self):
        doubleLinkedList = Double_Linked_List()
        doubleLinkedList.push("sdfsf")
        doubleLinkedList.push(1)
        doubleLinkedList.unshift(3)
        assert(list([doubleLinkedList.pop(), doubleLinkedList.pop(), doubleLinkedList.pop()]) == [1, "sdfsf", 3])

    def test_shift(self):
        doubleLinkedList = Double_Linked_List()
        doubleLinkedList.push("sdfsf")
        doubleLinkedList.push(1)
        doubleLinkedList.shift()
        assert(doubleLinkedList.pop() == 1)
        doubleLinkedList.shift()
        doubleLinkedList.shift()
        assert(doubleLinkedList.pop() == None)

    def test_delete1(self):
        doubleLinkedList = Double_Linked_List()
        doubleLinkedList.push("test1")
        doubleLinkedList.push(1)
        doubleLinkedList.push("test1")
        doubleLinkedList.push(2)
        doubleLinkedList.push("test1")
        doubleLinkedList.delete("test1")
        assert([doubleLinkedList.pop(), doubleLinkedList.pop()] == [2,1])

    def test_delete2(self):
        doubleLinkedList = Double_Linked_List()
        doubleLinkedList.push(1)
        doubleLinkedList.push(1)
        doubleLinkedList.push(1)
        doubleLinkedList.delete(1)
        assert(doubleLinkedList.pop() == None and doubleLinkedList.len() == 0 and doubleLinkedList.first() == None and doubleLinkedList.last() == None)
        
    
    def test_contains(self):
        doubleLinkedList = Double_Linked_List()
        doubleLinkedList.push("test1")
        doubleLinkedList.push(1)
        doubleLinkedList.push("test1")
        doubleLinkedList.push(2)
        doubleLinkedList.push("test1")
        assert(doubleLinkedList.containts("test1") and (doubleLinkedList.containts("sdzczxc")  == False))

    def test_first(self):
        doubleLinkedList = Double_Linked_List()
        doubleLinkedList.push("test1")
        doubleLinkedList.push(1)
        doubleLinkedList.push("test1")
        doubleLinkedList.delete("test1")
        assert(doubleLinkedList.first().elem == 1)

    def test_last(self):
        doubleLinkedList = Double_Linked_List()
        doubleLinkedList.push("test1")
        doubleLinkedList.push(1)
        doubleLinkedList.push(2)
        doubleLinkedList.delete("test1")
        assert(doubleLinkedList.last().elem == 2)
