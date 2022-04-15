class Node:
    def __init__(self, value=None, nextNode=None):
        self.value=value
        self.nextNode=nextNode

class Stack:
    def __init__(self):
        self.top=Node()
        self.size=0

    def push(self, data):
        newNode=Node(data)
        if self.top.value is None:
            self.top=newNode

        else:
            newNode.nextNode=self.top
            self.top = newNode

        self.size+=1

    def pop(self):
        data=self.top.value
        self.size-=1

        if self.top.value is None:
            print('Stack is empty, can not delete any Nodes')

        else:
            self.top=self.top.nextNode
        
        return data

    def printing(self):
        print(f' this is Top value: {self.top.value}')
        previousNode=self.top.nextNode
        while previousNode:
            print(previousNode.value)
            previousNode=previousNode.nextNode


if __name__ == '__main__':
    myStack=Stack()
    myStack.push(10)
    myStack.push(20)
    myStack.push(30)
    myStack.push(40)
    myStack.push(50)
    print('Imprimiendo antes de Pop: ')
    myStack.printing()
    print('Imprimiendo dps de Pop: ')
    myStack.pop()
    myStack.printing()
            
        