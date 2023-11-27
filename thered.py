import threading
import random 
import time
import datetime
class player:
    def __init__(self,n):
        self.names=n
        self.tt=threading.Thread(target=self.game)
        self.tt.start()


    def game(self):
        i=self.names
        n=random.randint(1,9)
        for m in range(n):
            print(f"player:{i},x pos={m}")
            agora = datetime.datetime.now()
            data_horas = agora.strftime("%S")
            data_hora = agora.strftime("%S")
            while(data_horas==data_hora):
                agora = datetime.datetime.now()
                data_horas = agora.strftime("%S")

        print(f"player:{i},is in is position")

    def endgame(self):
        self.tt.join()

print("\x1bc\x1b[43;30m")
players=3
t=[]
for n in range(players):
    tt=player(n)
    t=t+[tt]

for n in range(players):
    tt=t.pop()
    tt.endgame()