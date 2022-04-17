class Node:
    def __init__(self, value=None, nextNode=None, prevNode=None):
        self.value=value
        self.nextNode=nextNode
        self.prevNode=prevNode
        


class QueueNode:
    def __init__(self): #cuando necesitamos asignar valore en el constructor, no necesitamos incluir todas las variables al costado del self
        self.head=None
        self.tail=None
        self.count=0
        


    def enqueue(self, data):
        newNode=Node(data, None, None)
        if self.head is None:
            self.head=newNode
            self.tail=newNode #aqui se comporta como un pointer/variable

        else:
            self.tail.nextNode=newNode #pero aca vemos que self.tail se comporta como un nodo
            newNode.prevNode=self.tail
            self.tail=newNode

        self.count+=1

    def dequeue(self):
        currentNode=self.head
        if currentNode.value is None:
            print('The queue is empty!')

        else:
            subsequentNode=currentNode.nextNode
            currentNode=subsequentNode
            self.head=currentNode
            self.count -=1

   
    def traverse(self):
        currentNode=self.head
        while currentNode:
            print(currentNode.value)
            currentNode=currentNode.nextNode

         
if __name__ == '__main__':
    toto=QueueNode()
    toto.enqueue(1)
    toto.enqueue(2)
    toto.enqueue(3)
    toto.enqueue(4)
    toto.enqueue(5)
    toto.traverse()
    print('removiendo first item: ')
    toto.dequeue()
    toto.traverse()
    

