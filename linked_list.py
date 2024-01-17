class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singlell:
    def __init__(self):
        self.head = None
    
    def start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def travese(self):
        a = self.head
        while(a):
            print(a.data,end=" ")
            a = a.next

    def end(self,data):
        a = self.head
        ne = Node(data)
        while a.next is not None:
            a = a.next
        a.next = ne
    
    def position(self,data,pose):
        l = 0
        npn = Node(data)
        a = self.head
        for i in range(1,pose):
            a = a.next
        npn.next = a.next
        a.next = npn
        

s = singlell()
n1 =Node(7)
s.head =n1
s.end(9)
s.start(0)
s.start(1)
s.position(2,3)
s.travese()
