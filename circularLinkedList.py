class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data 
        self.nextNode = nextNode 


class CircularLinkedList:
    def __init__(self):
        self.head=Node()

    def prepend(self, data):
        currentNode=self.head
        newNode=Node(data, self.head) #el nuevo nodo siempre tiene que mirar a self.head
        
        

        if currentNode.nextNode is None: #si el linkelist esta vacio el primer nodo va a mirar a none
            newNode.nextNode=newNode #entonces hacemos que el nuevo node mire asi mismo en vez del viejo self.head
            self.head=newNode #y hacemos que newNode tome la posicion de self.head, es decir reemplazamos el nodo vacio

        else:
            while currentNode.nextNode != self.head: #si ya existe un nodo circular (no mira a None) vamos al ultimo
                currentNode=currentNode.nextNode
            currentNode.nextNode=newNode #una vez que lo hayamos hacemos que mire a newNode porque sera el nuevo self.head
            self.head=newNode #y cambiamnos de nombre
        
   
    def append(self, data):
        currentNode=self.head
        newNode=Node(data, self.head)

        if currentNode.nextNode is None:
            newNode.nextNode = newNode
            self.head=newNode

        else:
            while currentNode.nextNode != self.head:
                currentNode=currentNode.nextNode
            currentNode.nextNode=newNode
            


    def print_list(self):
        currentNode = self.head 

        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.nextNode
            if currentNode == self.head:
                break


if __name__== '__main__':
    cllist = CircularLinkedList()
    cllist.append("C")
    cllist.append("D")
    cllist.prepend("B")
    cllist.prepend("A")
    cllist.prepend("Z")
    cllist.print_list()
            
           
            
            


  