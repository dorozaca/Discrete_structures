class ListQueue:
    def __init__(self): #cuando necesitamos asignar valore en el constructor, no necesitamos incluir todas las variables al costado del self
        self.items=[]
        self.size=0

    def enqueue(self, data):
        self.items.insert(0,data)
        self.size+=1

    def dequeue(self):
        data=self.items.pop()
        self.size-=1
        return data

    def traverse(self):
        for i in range(self.size):
            print(self.items[i])
            #print(f'There are {self.size} elements')

if __name__ == '__main__':
    breakfast=ListQueue()
    breakfast.enqueue('Bacon')
    breakfast.enqueue('Eggs')
    breakfast.enqueue('Milk')
    breakfast.enqueue('Toast')
    

    breakfast.traverse()
    print()

    breakfast.dequeue()

    breakfast.traverse()








