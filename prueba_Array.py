class myArray:
    def __init__(self, size, fillvalue=None):
        self.myArrayi=[]
        self.size=size
        self.fillvalue=fillvalue
        for i in range(self.size):
            self.myArrayi.append(self.fillvalue)
       

    def __insert__(self, value):
        for i in range(len(self.myArrayi)):
            if self.myArrayi[i] is None:
                self.myArrayi[i]=value
                break
        
    def __remove__(self):
        self.myArrayi.pop()

    def __print__(self):
        for i in range(len(self.myArrayi)):
            print(self.myArrayi[i])

    def __get__(self, index):
        for i in range(len(self.myArrayi)):
            if i==index:
                return self.myArrayi[i]

if __name__== '__main__':
    Diego=myArray(5)
    Diego.__insert__(50) 
    Diego.__insert__(60) 
    Diego.__insert__(70) 
    Diego.__insert__(80) 
    Diego.__insert__(90)
    Diego.__print__()
    print(Diego.myArrayi)
    Diego.__remove__()
    Diego.__print__()
    print(f' La posicion 1 es {Diego.__get__(1)}') 

        

        






