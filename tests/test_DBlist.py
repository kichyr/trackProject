import pytest
import sys
sys.path.append("/home/kichyr/trackProject/app/hw2")
from double_linked_list import DoubleLinkedList

class  Test_DoubleLinkedList:
    def test_negative(self):
        doubleLinkedList = DoubleLinkedList()
        assert((doubleLinkedList.push(None)) == None and doubleLinkedList.len() == 1)

    def test_push_pop(self):
        doubleLinkedList = DoubleLinkedList()
        doubleLinkedList.push("sdfsf")
        doubleLinkedList.push(1)
        assert(list([doubleLinkedList.pop(), doubleLinkedList.pop(), doubleLinkedList.pop()]) == [1, "sdfsf", None])

    def test_unshift(self):
        doubleLinkedList = DoubleLinkedList()
        doubleLinkedList.push("sdfsf")
        doubleLinkedList.push(1)
        doubleLinkedList.unshift(3)
        assert(list([doubleLinkedList.pop(), doubleLinkedList.pop(), doubleLinkedList.pop()]) == [1, "sdfsf", 3])
    
    def test_unshift(self):
        doubleLinkedList = DoubleLinkedList()
        doubleLinkedList.push("sdfsf")
        doubleLinkedList.push(1)
        doubleLinkedList.unshift(3)
        assert(list([doubleLinkedList.pop(), doubleLinkedList.pop(), doubleLinkedList.pop()]) == [1, "sdfsf", 3])

    def test_shift(self):
        doubleLinkedList = DoubleLinkedList()
        doubleLinkedList.push("sdfsf")
        doubleLinkedList.push(1)
        doubleLinkedList.shift()
        assert(doubleLinkedList.pop() == 1)
        doubleLinkedList.shift()
        doubleLinkedList.shift()
        assert(doubleLinkedList.pop() == None)

    def test_delete1(self):
        doubleLinkedList = DoubleLinkedList()
        doubleLinkedList.push("test1")
        doubleLinkedList.push(1)
        doubleLinkedList.push("test1")
        doubleLinkedList.push(2)
        doubleLinkedList.push("test1")
        doubleLinkedList.delete("test1")
        assert([doubleLinkedList.pop(), doubleLinkedList.pop()] == [2,1])

    def test_delete2(self):
        doubleLinkedList = DoubleLinkedList()
        doubleLinkedList.push(1)
        doubleLinkedList.push(1)
        doubleLinkedList.push(1)
        doubleLinkedList.delete(1)
        assert(doubleLinkedList.pop() == None and doubleLinkedList.len() == 0 and doubleLinkedList.first() == None and doubleLinkedList.last() == None)
        
    
    def test_contains(self):
        doubleLinkedList = DoubleLinkedList()
        doubleLinkedList.push("test1")
        doubleLinkedList.push(1)
        doubleLinkedList.push("test1")
        doubleLinkedList.push(2)
        doubleLinkedList.push("test1")
        assert(doubleLinkedList.containts("test1") and (doubleLinkedList.containts("sdzczxc")  == False))

    def test_first(self):
        doubleLinkedList = DoubleLinkedList()
        doubleLinkedList.push("test1")
        doubleLinkedList.push(1)
        doubleLinkedList.push("test1")
        doubleLinkedList.delete("test1")
        assert(doubleLinkedList.first().elem == 1)

    def test_last(self):
        doubleLinkedList = DoubleLinkedList()
        doubleLinkedList.push("test1")
        doubleLinkedList.push(1)
        doubleLinkedList.push(2)
        doubleLinkedList.delete("test1")
        assert(doubleLinkedList.last().elem == 2)
