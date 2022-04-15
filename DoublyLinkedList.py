class Node:
    def __init__(self, value=None, nextNode=None, prevNode=None):
        self.value=value
        self.nextNode=nextNode
        self.prevNode=prevNode


class DoublyLinkedList:
    def __init__(self):
        self.head=Node()
        
    def append(self, value):
        newNode=Node(value)
        currentNode=self.head
        if currentNode.value is None:
            self.head=newNode
        
        else:
            while currentNode.nextNode is not None:
                currentNode=currentNode.nextNode
            newNode.prevNode=currentNode
            currentNode.nextNode=newNode

    def printing(self):
        currentNode=self.head
        while currentNode:
            print(currentNode.value)
            currentNode=currentNode.nextNode

    def prepend(self, value):
        currentNode=self.head
        newNode=Node(value)

        if currentNode.value is None:
            self.head=newNode

        else:
            currentNode.prevNode=newNode
            newNode.nextNode=currentNode
            self.head=newNode

    def get(self, index):
        currentNode=self.head
        myindex=0
        
        while currentNode:
            if myindex==index:
                return currentNode.value
            currentNode=currentNode.nextNode
            myindex+=1    
    
    def set(self, index, myvalue):
        currentNode=self.head
        myindex=0
        
        while currentNode:
            if myindex==index:
                currentNode.value=myvalue
                return
            currentNode=currentNode.nextNode
            myindex+=1    

    def remove(self, index):
        currentNode=self.head
        
        myindex=0
        
        while currentNode:
            previousNode=currentNode.prevNode
            if myindex==index:
                previousNode.nextNode=currentNode.nextNode
                return
            currentNode=currentNode.nextNode
            myindex+=1  

              

if __name__ == '__main__':
    dllist=DoublyLinkedList()
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.append(5)
    dllist.prepend(0)
    dllist.prepend(-1)
    dllist.printing()
    print('testing get method')
    print(dllist.get(1))
    print()
    print('testing set index 1')
    dllist.set(1,100)
    dllist.printing()
    print('Testing removing')
    dllist.remove(1)
    dllist.printing()