import threading
import random 
import time
import datetime
scores=0
class taskgest:
    def __init__(self,players):
        global sss
        self.t=[]
        for n in range(players):
            tt=player(n)
            self.t=self.t+[tt]

        for n in range(players):
            tt=self.t.pop()
            tt.endgame()


        sss.endss()
        sss.endgame()


class queque:
    def __init__(self):
        self.enable=False
        
    def releases(self):
        self.enable=False


    def gets(self):
        enables=True
        while enables:
            if not self.enable:
                self.enable=True
                return 0
            else:
                while not self.enable:
                    pass
class spoll:
    def __init__(self):
        self.lists=[]
        self.ends=False
        self.tt=threading.Thread(target=self.agenda)
        self.tt.start()
        

    def endss(self):
        self.ends=True


    def agenda(self):
        while not self.ends or len(self.lists)!=0:
            if len(self.lists)>0:
                print(self.lists.pop(0))
                
        
        
    def prints(self,s):
        self.lists=self.lists+[s]


    def endgame(self):
        self.tt.join()

class player:
    def __init__(self,n):
        self.names=n
        self.s=""
        self.counter=0
        self.tt=threading.Thread(target=self.game)
        self.tt.start()
        


    def game(self):
        global queque1
        global scores
        i=self.names
        n=random.randint(1,9)
        for m in range(n):
            self.printss(f"player:{i},x pos={m}")
            queque1.gets()
            scores+=100
            self.printss(f"score:{scores}")
            self.sends()
            queque1.releases()
            self.timers(1)

        self.printss(f"player:{i},is in is position")
        self.sends()
    
    def timers(self,s):
        time.sleep(s)
 


    def printss(self,s):
        if self.counter!=0:
            self.s=self.s+"\n"
        self.s=self.s+s
        self.counter+=1


    def sends(self):
        global sss
        sss.prints(self.s[:])
        self.s=""
        self.counter=0
        
    def endgame(self):
        self.tt.join()

print("\x1bc\x1b[43;30m")
players=3

queque1=queque()
sss=spoll()
gest=taskgest(players)