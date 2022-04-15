from email import header
from hashlib import new
import random


class myArray:
    def __init__(self, length, fillvalue=None):
        self.mylist=[]    #This is what you need to memorize
        self.length=length
        for i in range(length):
            self.mylist.append(fillvalue)
        

    def __len__(self):
        return len(self.mylist)

    def __str__(self):
        return str(self.mylist)

    def __iter__(self):
        return iter(self.mylist)

    def __getitem__(self, index):
        for i in range(self.length):
            if index==i:
                return self.mylist[i]

    def __setitem__(self, index, value):
        for i in range(self.length):
            if index == i:
                self.mylist[i]=value

    def __myrandom__(self):
       myrandom=list(random.randint(1,50) for i in range(self.length))
       for i in range(self.length):
           self.mylist[i]=myrandom[i]
       return self.mylist 
       

    def __sumaitems__(self):
        counter=0
        for i in range(self.length):
            counter+=self.mylist[i]

        return counter

class MultiArray(myArray):

    def __init__(self, rows, cols, fillvalue=None):
        self.myarray=myArray(rows)
        for i in range(self.myarray.__len__()):
            self.myarray[i]=myArray(cols, fillvalue)
         

    def get_height(self):
        return self.myarray.__len__()

    def get_width(self):
        return len(self.myarray[0])

    def __str__(self):
        for i in self.myarray:
            print('\t'.join(map(str,i)))

class Node:

    def __init__(self, value=None, nextNode=None):
        self.value=value
        self.nextNode=nextNode

class Linkedlist:

    def __init__(self):
        self.head=Node()

    def insert(self, value):
        currentNode=self.head
        newNode=Node(value)
        while currentNode.nextNode is not None:
            currentNode=currentNode.nextNode
        currentNode.nextNode=newNode

    def display(self):
        originalNode=self.head
        currentNode=originalNode.nextNode

        while currentNode.value is not None:
            print(currentNode.value)
            currentNode=currentNode.nextNode

    def getmyItem(self, index):
        currentNode=self.head
        myindex=-1
        while currentNode is not None:
            if myindex==index:
                return currentNode.value
            currentNode=currentNode.nextNode
            myindex+=1

    def erasetem(self, index):
        currentNode=self.head
        myindex=0
        while True:
            lastNode=currentNode
            currentNode=currentNode.nextNode
            if index==myindex:
                lastNode.nextNode=currentNode.nextNode
                return
            myindex+=1

class CircularLinkedList:
    def __init__(self):
        self.head=Node()

    def append(self, value):
        currentNode=self.head
        newNode=Node(value, self.head)

        if currentNode.nextNode is None:
            newNode.nextNode=newNode
            self.head=newNode
            

        else:
            while currentNode.nextNode != self.head:
                currentNode=currentNode.nextNode
            currentNode.nextNode=newNode

    def prepend(self, value):
        currentNode=self.head
        newNode=Node(value, self.head)

        if currentNode.nextNode is None:
            newNode.nextNode=newNode
            self.head=newNode

        else:
            while currentNode.nextNode != self.head:
                currentNode=currentNode.nextNode
            currentNode.nextNode=newNode
            self.head=newNode

    def printing(self):
        currentNode=self.head
        while currentNode.nextNode !=self.head:
            print(currentNode.value)
            currentNode=currentNode.nextNode
        print(currentNode.value)





            
if __name__== '__main__':
   ###### Array Tests #########
   print('*' *20 + ' Array Tests' + '*' *20 )
   Diego=myArray(5)
   print(Diego)

   for i in range(len(Diego)):
        Diego[i]=i+2
   print(Diego)

   Diego.__myrandom__()
   print(Diego)

   print(Diego.__iter__)
   print(Diego.__getitem__(4))
   Diego.__setitem__(2,80)
   print(Diego)
   print(Diego.__sumaitems__())
   print()
   
   ###### Grid Tests #########
   print('*' *20 + ' Grid Tests' + '*' *20)

   toto=MultiArray(5,4,'x')
   toto.__str__()

   ###### LinkedList Tests #########
   print('*' *20 + ' Linked List Tests' + '*' *20)
   mylink=Linkedlist()
   mylink.insert(5)
   mylink.insert(6)
   mylink.insert(7)
   mylink.insert(8)
   mylink.insert(None)
   
   mylink.display()
   print('Item in index 1:')
   print(mylink.getmyItem(1))
   print('erasing item in index 1')
   mylink.erasetem(1)
   mylink.display()

   ###### Circular LinkedList Tests #########
   print('*' *20 + ' Linked List Tests' + '*' *20)
   mylink=CircularLinkedList()
   mylink.append('C')
   mylink.append('D')
   mylink.append('E')
   mylink.append('F')
   mylink.append('G')
   mylink.printing()
   print('/n' + 'Imprimiendo')

   mylink.prepend('B')
   mylink.prepend('A')
   
   
     
   mylink.printing()
  


        

        






