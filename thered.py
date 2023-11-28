import threading
import random 
import time
import datetime
scores=0
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
                enables=False
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
        for n in range(s):
            agora = datetime.datetime.now()
            data_horas = agora.strftime("%S")
            data_hora = agora.strftime("%S")
            while(data_horas==data_hora):
                agora = datetime.datetime.now()
                data_horas = agora.strftime("%S")




    def printss(self,s):
        self.s=self.s+s+"\n"


    def sends(self):
        global sss
        sss.prints(self.s[:])
        self.s=""
        
    def endgame(self):
        self.tt.join()

print("\x1bc\x1b[43;30m")
players=3
t=[]
queque1=queque()
sss=spoll()
for n in range(players):
    tt=player(n)
    t=t+[tt]

for n in range(players):
    tt=t.pop()
    tt.endgame()


sss.endss()
sss.endgame()