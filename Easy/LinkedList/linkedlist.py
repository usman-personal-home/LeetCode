from node import Node


class UnorderedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, val):
        temp = Node(val)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, val):

        if self.search(val) is False:
            raise Exception("Cannot remove, element does not exist")

        # search for the element
        found = False
        cur = self.head
        previous = None

        while not found:
            if cur.getData() == val:
                found = True
            else:
                previous = cur
                cur = cur.getNext()

        if previous is None:
            self.head = cur.getNext()
        else:
            previous.setNext(cur.getNext())

    def size(self):
        sz = 0
        if self.isEmpty():
            sz = 0
        cur = self.head

        while cur is not None:
            sz += 1
            cur = cur.getNext()
        return sz

    def search(self, val):
        found = False
        if self.isEmpty():
            return found

        cur = self.head
        while cur is not None and not found:
            if cur.getData() == val:
                found = True
            else:
                cur = cur.getNext()

        return found

    def append(self, val):

        cur = self.head

        while cur.getNext() is not None:
            cur = cur.getNext()

        cur.setNext(Node(val))

    def lprint(self):
        cur = self.head
        while cur is not None:
            print(cur.getData())
            cur = cur.getNext()

    def toArray(self):
        lst = []
        cur = self.head
        while cur is not None:
            lst.append(cur.getData())
            cur = cur.getNext()
        return lst

"""
ll = UnorderedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(7)
ll.lprint()


print("***********************")
ll.append(8)

print("***********************")
ll.lprint()
#ll.remove(4)
print("***********************")
#print(ll.search(6))
#print(ll.search(8))
#print(ll.size())
#ll.lprint()
print("***********************")
"""


class OrderedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, val):

        # search for the element
        cur = self.head
        previous = None
        stop = False

        while cur is not None and not stop:
            if cur.getData() > val:
                stop = True
            else:
                previous = cur
                cur = cur.getNext()

        temp = Node(val)

        # check to see if empty linked list
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(cur)
            previous.setNext(temp)

        """
        cur = self.head
        temp = Node(val)
        if self.head is None:
            self.head = temp
        else:
            while cur.getNext() is not None and cur.getNext().data <= val:
                cur = cur.getNext()
                temp.setNext(cur.getNext())
                cur.setNext(temp)
        """



    def remove(self, val):

        if self.search(val) is False:
            raise Exception("Cannot remove, element does not exist")

        # search for the element
        found = False
        cur = self.head
        previous = None

        while not found:
            if cur.getData() == val:
                found = True
            else:
                previous = cur
                cur = cur.getNext()

        if previous is None:
            self.head = cur.getNext()
        else:
            previous.setNext(cur.getNext())

    def size(self):
        sz = 0
        if self.isEmpty():
            sz = 0
        cur = self.head

        while cur is not None:
            sz += 1
            cur = cur.getNext()
        return sz

    def search(self, val):
        counter = 0
        found = False
        stop = False
        cur = self.head

        while cur is not None and not found and not stop:
            counter += 1

            if cur.getData() == val:
                found = True
            elif cur.getData() > val:
                print("in here")
                stop = True
            else:
                cur = cur.getNext()

        print(counter)
        return found

    def lprint(self):
        cur = self.head
        while cur is not None:
            print(cur.getData())
            cur = cur.getNext()

    def toArray(self):
        lst = []
        cur = self.head
        while cur is not None:
            lst.append(cur.getData())
            cur = cur.getNext()
        return lst

if __name__ == '__main__':
    lo = OrderedList()
    lo.add(2)

    lo.add(9)
    lo.add(3)
    lo.add(4)
    lo.add(1)
    lo.add(25)
    lo.add(2)
    lo.add(40)
    print("***********************")
    #lo.lprint()
    print("***********************")
    print(lo.search(40))
    print("***********************")
    #print(lo.search(8))
    #print(lo.size())
    lo.lprint()
    print(lo.toArray())
    print("***********************")
