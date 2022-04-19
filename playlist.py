from asyncio import current_task


class Node:

    def __init__(self, value=None, nextNode=None):
        self.value=value
        self.nextNode=nextNode


class Playlist:

    def __init__(self):
        self.head=Node()
        self.tail=None

    def addingSongs(self, title):
        newSong=Node(title)
        currentNode=self.head

        if currentNode.value is None:
            self.head=newSong
            self.tail=newSong

        else:
            self.tail.nextNode=newSong
            self.tail=newSong

    def playSong(self):

        currentSong=self.head
        subsequentSong=currentSong.nextNode
        self.head=subsequentSong

    def showplaylist(self):

        currentsong=self.head
        while currentsong:
            print(currentsong.value)
            currentsong=currentsong.nextNode

        
if __name__ == '__main__':
    mylist=Playlist()
    mylist.addingSongs('Tk')
    mylist.addingSongs('Zen')
    mylist.addingSongs('Kiss')
    mylist.addingSongs('PSV')
    mylist.addingSongs('Keane')

    mylist.showplaylist()
    print('reproduciendo una cancion: ')
    mylist.playSong()
    mylist.showplaylist()


    