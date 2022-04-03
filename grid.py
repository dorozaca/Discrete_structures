from myarray import Array

class Grid(Array):

    def __init__(self, rows, cols, fill_value='X'):
        self.data=Array(rows)
        for i in range(rows):
            self.data[i]=Array(cols, fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __str__(self):

       for i in self.data:
           print('\t'.join(map(str,i)))

       
       


if __name__=='__main__':

    toto=Grid(5,4)
    toto.__str__()



     
    
  



