class Node:

#This function declares the Node that should be appended to the LL
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:

    #Initializing a new LinkedList
    def __init__(self):
        self.head = None

    #Insert Node at the end
    def insert(self,value):
        if self.head is None:
            self.head = Node(value,None)
            return

        itr = self.head
        while itr.next != None:
            itr = itr.next

        itr.next = Node(value,None)

    #function to check length of LL
    def checkcount(self):
        if self.head is None:
            return 0

        itr = self.head
        count = 1

        while itr.next:
            itr = itr.next
            count+=1

        return count


    def insert_at_pos(self,pos,value):
        check = self.checkcount()

        if check+1 == pos:
            self.insert(value)
        elif check < pos:
            print('The list is not long enough')
            return
        else:
            itr = self.head
            while pos-1:
                itr = itr.next
                pos-=1

            temp = itr.next
            itr.next = Node(value, None)
            itr = itr.next
            itr.next = temp

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
    NLL.insert(1)
    NLL.insert(2)
    NLL.insert(3)
    NLL.insert(4)
    NLL.insert(5)
    NLL.insert(6)
    NLL.insert_at_pos(5,7)
    NLL.print()
