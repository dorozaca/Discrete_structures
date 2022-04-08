class Node():
    def __init__(self, data, nextNode=None):
        self.data=data
        self.nextNode=nextNode

# node1 = Node(20)
# node2=Node(40,node1)
# node3=Node(50,node2)
# node4=Node(60,node3)
# node5=Node(70,node4)

# currentNode=node5
# while currentNode.nextNode != None:
#     print (f'{currentNode.data} , ->') 
#     currentNode=currentNode.nextNode

class Linked_list:
    def __init__(self, head=None):
        self.head=head

    def insert(self, data):
        node=Node(data)
        
        if self.head is None:
            self.head=node
            return

        currentNode=self.head
        while currentNode.nextNode is not None:
            currentNode=currentNode.nextNode
        
        currentNode.nextNode=node

    def printLinkedList(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode=currentNode.nextNode
        print('No nodes')
        

if __name__== '__main__':
    mylink=Linked_list()
    mylink.insert(5)
    mylink.insert(6)
    mylink.insert(7)
    mylink.printLinkedList()


            







