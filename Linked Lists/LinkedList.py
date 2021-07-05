class Node:

#This function declares the Node that should be appended to the LL
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class LinkedList:

    #Initializing a new LinkedList
    def __init__(self):
        self.head = None

    #Insert Node into Head
    def insert_at_beginning(self,value):
        node = Node(value, self.head)
        self.head = node

    #Insert Node at the end
    def insert_at_end(self,value):
        if self.head is None:
            self.head = Node(value,None)
            return

        itr = self.head
        while itr.next != None:
            itr = itr.next

        itr.next = Node(value,None)

    #Print the Linked List
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = []
        while itr:
            llstr.append(itr.value)
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    NLL = LinkedList()
    NLL.insert_at_beginning(1)
    NLL.insert_at_beginning(2)
    NLL.insert_at_beginning(3)
    NLL.insert_at_beginning(4)
    NLL.insert_at_beginning(5)
    NLL.insert_at_end(6)
    NLL.insert_at_pos(4,7)
    NLL.print()
