import random


class Array:
    def __init__(self, capacity, fill_value=None):
        self.items=list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index]=value

    def __myrandom__(self):
        
        container=list(random.randint(20,50) for i in range(50))
        for i in range(len(self.items)):
            self.__setitem__(i, container[i])
       


if __name__=='__main__':
    Diego=Array(5)
    print(Diego)

    for i in range(len(Diego)):
        Diego[i]=i+2
    print(Diego)

    Diego.__myrandom__()
    print(Diego)

    print(Diego.__iter__)
    Diego.__getitem__(4)
    Diego.__setitem__(2,80)
