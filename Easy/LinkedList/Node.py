class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def getval(self):
        return self.val

    def getNext(self):
        return self.next

    def setval(self, newval):
        self.val = newval

    def setNext(self, newnext):
        self.next = newnext


if __name__ == '__main__':
    n = Node()
