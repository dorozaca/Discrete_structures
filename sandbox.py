from myarray import Array
# lista=['naranda', 'papaya', 'mango']
# lista.remove('mango')
# lista.insert(0, 'fresa')
# print(lista)

# mitupla='perro','gato','leon',
# print(type(mitupla))
# mitupla2=(5,6,8)
# print(mitupla2)

# myset={5,5,4,4,8,8,9,9}
# print(myset)

# myd={'Peru':500, 'Colombia':600, 'Ecuador':700}
# myd2=dict([('Peru',500),('Colombia',600),('Ecuador',700)])
# myd3=dict(Peru=500, Colombia=600, Ecuador=700)
# print(myd,myd2,myd3)

class Multi_Array(Array):
    def __init__(self, rows, cols, fillvalue=None):
        self.data=Array(rows)
        for i in range(rows):
            self.data[i]=Array(cols, fillvalue)

    def __str__(self):
        for i in self.data:
            print('\t'.join(map(str,i)))

    def getwidth(self):
        return len(self.data)

    def getheigth(self):
        return len(self.data[0])

class Node:
    def __init__(self, data=None, nextNode=None):
        self.data=data
        self.nextNode=nextNode
   

class LinkList:
    def __init__(self):
        self.head=Node()
       
    def insert(self, value):
        
        newNode=Node(value)
        currentNode=self.head
        while currentNode.nextNode is not None:
            currentNode=currentNode.nextNode
        currentNode.nextNode=newNode

    
    def length(self):
        currentNode=self.head
        counter=0
        while currentNode.nextNode is not None:
            counter +=1
            currentNode=currentNode.nextNode
        return counter

    def print(self):
        currentNode=self.head
        while currentNode.nextNode is not None:
            print(currentNode.data)
            currentNode=currentNode.nextNode

    
        
    
  
       

    
if __name__ == '__main__':
    mitest=Multi_Array(5,4)
    mitest.__str__()
    mitest.getheigth()
    print(dir(mitest))

    ########LinkedList#############
   
    mylink=LinkList()
    mylink.insert(20)
    mylink.insert(40)
    mylink.insert(50)
    mylink.insert(60)
    mylink.insert(70)
    mylink.insert(80)
    print('La longitud es: ')
    print(mylink.length())
    mylink.print()
       
    
    
    