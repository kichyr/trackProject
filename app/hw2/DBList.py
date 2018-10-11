#element of list
class Item:
    def __init__(self, elem, next_item=None, prev_item=None):
        self.elem = elem
        self.next_item = next_item
        self.prev_item = prev_item

#double linked list
class Double_Linked_List:

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__length = 0

    """
    high level support for doing this and that.
    """
    def push(self, elem):
        if self.__first is None:
            self.__first = Item(elem, None, None)
            self.__last = self.__first
            self.__length += 1
        else:
            self.__last.next_item = Item(elem, None, self.__last)
            self.__last = self.__last.next_item
            self.__length += 1

    def pop(self):
        if self.__length > 0:
            last = self.__last
            if self.__length == 1:
                self.__first = None
                self.__last = None
                self.__length -= 1
            else:
                self.__last = self.__last.prev_item
                self.__last.next_item = None
                self.__length -= 1
            return last.elem
        else:
            return None

    def unshift(self, elem):
        if self.__length > 0:
            self.__first.prev_item = Item(elem, self.__first, None)
            self.__first = self.__first.prev_item
            self.__length += 1
        else:
            self.__first = Item(elem, None, None)
            self.__last = self.__first
            self.__length += 1

    def shift(self):
        if self.__length > 0:
            self.__first = self.__first.next_item
            self.__first.prev_item = None
            self.__length -= 1

    def len(self):
        return self.__length

    def delete(self, elem):
        iterator = self.__first
        while iterator is not None:
            if iterator.elem == elem:
                self.__length -= 1
                if iterator.prev_item is not None:
                    iterator.prev_item.next_item = iterator.next_item
                if iterator.next_item is not None:
                    iterator.next_item.prev_item = iterator.prev_item
                if iterator == self.__first:
                    if iterator.next_item is not None:
                        self.__first = iterator.next_item
                    else:
                        self.__first = None
                if iterator == self.__last:
                    if iterator.prev_item is not None:
                        self.__last = iterator.prev_item
                    else:
                        self.__last = None
            iterator = iterator.next_item

    def containts(self, elem):
        iterator = self.__first
        while iterator is not None:
            if iterator.elem == elem:
                return True
            iterator = iterator.next_item
        return False
    def first(self):
        return self.__first

    def last(self):
        return self.__last
