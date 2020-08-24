import time 
import random
class Winamp():
    def __init__(self,songs=[]):
        self.power=True
        self.songs=songs
        self.volume=100
        self.currentSong=""

    def incVolume(self):
        if(self.volume >= 95):
            pass
        else:
            print("Increasing volume")
            time.sleep(2)
            self.volume +=5
            print("Volume level : {}".format(self.volume))

    def decVolume(self):
          if(self.volume<=0):
              pass      
          else:
              print("Decreasing volume")
              self.volume -= 5  
              print("Volume level : {}".format(self.volume))
 
    def songList(self):
        print(self.songs)

    def addSong(self,song):
        self.songs.append(song)         
    
    def choose(self):
        for i in self.songs:
            print("{}".format(i))
        choice=int(input("Choose a song number: "))
        print("Changing the song")
        time.sleep(2)
        self.currentSong=self.songs[choice-1]     
        print("Current song: {}".format(self.currentSong))

    def mixSong(self):
        randomNumber=random.randint(0,len(self.songs))
        self.currentSong=self.songs[randomNumber]

    def onOff(self):   
        self.power=False 
    
    def delete(self):
        choicee=int(input("Which song would you like to delete? : "))
        self.songs.pop(choicee-1)

    def	interface(self):
        print(""" 
        Song List = {}
        Current Song= {}
        Volume= {}
        Power= {}
        
        1-Choose a song
        2-Increase volume
        3-Decrease volume
        4-Random song
        5-Add new song
        6-Delete song
        7-Turn off
        """.format(self.songs,self.currentSong,self.volume,self.power))     

o1=Winamp(songs=["1-Beautiful Tango","2-Oursoul","3-Nothing Else","4-From the Stalls","5-Mice"])
while True:
    o1.interface()
    choice=int(input("What do you want? : "))
    if(choice==1):
        o1.choose()
    elif(choice==2):
        o1.incVolume()
    elif(choice==3):
        o1.decVolume()
    elif(choice==4):
        o1.mixSong()
    elif(choice==5):
        s=input("Song name: ")
        o1.addSong(s)
    elif(choice==6):
        o1.delete()
    elif(choice==7):
        o1.onOff()              
            
